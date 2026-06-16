from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from data import calculate_eligibility_score, get_best_bank, calculate_max_loan_amount, get_education_loan_info
app = Flask(__name__)
app.config['SECRET_KEY'] = 'loansense-secret-key-2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loansense.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    monthly_income = db.Column(db.Float, default=0)
    monthly_expenses = db.Column(db.Float, default=0)
    cibil_score = db.Column(db.Integer, default=750)
    loan_type = db.Column(db.String(50), default='home_loan')
    onboarded = db.Column(db.Boolean, default=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('❌ Invalid email or password. Please try again.')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('❌ Email already registered. Please login.')
            return redirect(url_for('login'))
        hashed_password = generate_password_hash(password)
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('onboarding'))
    return render_template('login.html')

@app.route('/onboarding', methods=['GET', 'POST'])
@login_required
def onboarding():
    if request.method == 'POST':
        current_user.monthly_income = float(request.form.get('monthly_income', 0))
        current_user.monthly_expenses = float(request.form.get('monthly_expenses', 0))
        current_user.cibil_score = int(request.form.get('cibil_score', 750))
        current_user.loan_type = request.form.get('loan_type', 'home_loan')
        current_user.onboarded = True
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('onboarding.html')

@app.route('/documents', methods=['GET', 'POST'])
@login_required
def documents():
    from data import DOCUMENT_REQUIREMENTS
    from module1_document_verifier.extractor import verify_document
    import PyPDF2

    loan_type = current_user.loan_type or "home_loan"
    docs_required = DOCUMENT_REQUIREMENTS.get(loan_type, DOCUMENT_REQUIREMENTS["home_loan"])
    total_docs = len([d for d in docs_required["documents"] if d["mandatory"]])

    verification_result = None

    if request.method == 'POST':
        if 'document' in request.files:
            file = request.files['document']
            if file.filename != '':
                # Read PDF text
                try:
                    reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page in reader.pages:
                        text += page.extract_text() or ""

                    if text.strip():
                        verification_result = verify_document(text)
                    else:
                       verification_result = {
                          "pan_number": None,
                         "income": None,
                           "anomalies": [
                               "⚠️ This file appears to be corrupted or is not a valid PDF.",
                              "Please upload a proper text-based PDF document.",
                                "Scanned image PDFs may not work — use original digital documents."
                            ]
                        }
                except Exception as e:
                    verification_result = {
                        "pan_number": None,
                        "income": None,
                        "anomalies": [f"Error reading file: {str(e)}"]
                    }

    return render_template('documents.html',
                         user=current_user,
                         docs_required=docs_required,
                         total_docs=total_docs,
                         uploaded_docs=0,
                         verification_result=verification_result)

@app.route('/dashboard')
@login_required
def dashboard():
    from data import calculate_eligibility_score, get_best_bank, DOCUMENT_REQUIREMENTS
    
    score = calculate_eligibility_score(
        income=current_user.monthly_income or 60000,
        expenses=current_user.monthly_expenses or 20000,
        existing_emis=0,
        cibil_score=current_user.cibil_score or 750,
        age=30,
        employment_type="salaried"
    )

    loan_type = current_user.loan_type or "home_loan"
    best_banks = get_best_bank(loan_type, 5000000, current_user.cibil_score or 750)
    docs_required = DOCUMENT_REQUIREMENTS.get(loan_type, DOCUMENT_REQUIREMENTS["home_loan"])
    total_docs = len([d for d in docs_required["documents"] if d["mandatory"]])

    return render_template('dashboard.html',
                         user=current_user,
                         eligibility_score=score,
                         best_banks=best_banks[:3],
                         docs_required=docs_required,
                         total_docs=total_docs,
                         uploaded_docs=0)
<<<<<<< HEAD
=======
@app.route('/bank-compare')
@login_required
def bank_compare():
    from data import BANK_DATA, get_best_bank
    import json
    loan_type = request.args.get('type', current_user.loan_type or "home_loan")
    all_banks = get_best_bank(loan_type, 5000000, current_user.cibil_score or 750)
    banks_json = json.dumps([{"name": b["name"], "rate": b["rate"]} for b in all_banks])
    return render_template('bank_compare.html',
                         user=current_user,
                         banks=all_banks,
                         loan_type=loan_type,
                         bank_data=BANK_DATA,
                         banks_json=banks_json)

>>>>>>> feature-bank-comparison
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)