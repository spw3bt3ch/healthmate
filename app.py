
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from calculations import bmi, whr, bmr, stroke_score, arthritis_score

app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-this-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthmate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    test = db.Column(db.String(120), nullable=False)
    value = db.Column(db.String(64), nullable=False)
    category = db.Column(db.String(64), nullable=False)
    message = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi', methods=['GET','POST'])
def bmi_route():
    result = None
    if request.method == 'POST':
        try:
            weight = float(request.form.get('weight'))
            height = float(request.form.get('height'))
            res = bmi(weight, height)
            result = res
            db.session.add(History(test='BMI', value=res.value, category=res.category, message=res.message))
            db.session.commit()
        except Exception as e:
            flash('Invalid input. Please check your values.')
    return render_template('bmi.html', result=result)

@app.route('/whr', methods=['GET','POST'])
def whr_route():
    result = None
    if request.method == 'POST':
        try:
            waist = float(request.form.get('waist'))
            hip = float(request.form.get('hip'))
            gender = request.form.get('gender','F')
            res = whr(waist, hip, gender)
            result = res
            db.session.add(History(test='WHR', value=res.value, category=res.category, message=res.message))
            db.session.commit()
        except:
            flash('Invalid input.')
    return render_template('whr.html', result=result)

@app.route('/bmr', methods=['GET','POST'])
def bmr_route():
    result = None
    if request.method == 'POST':
        try:
            gender = request.form.get('gender','F')
            weight = float(request.form.get('weight'))
            height = float(request.form.get('height'))
            age = int(request.form.get('age'))
            res = bmr(weight, height, age, gender)
            result = res
            db.session.add(History(test='BMR', value=res.value, category=res.category, message=res.message))
            db.session.commit()
        except:
            flash('Invalid input.')
    return render_template('bmr.html', result=result)

@app.route('/stroke', methods=['GET','POST'])
def stroke_route():
    result = None
    if request.method == 'POST':
        try:
            age = int(request.form.get('age'))
            high_bp = request.form.get('high_bp') == 'on'
            smoker = request.form.get('smoker') == 'on'
            diabetes = request.form.get('diabetes') == 'on'
            high_chol = request.form.get('high_chol') == 'on'
            inactive = request.form.get('inactive') == 'on'
            res = stroke_score(age, high_bp, smoker, diabetes, high_chol, inactive)
            result = res
            db.session.add(History(test='Stroke Risk', value=res.value, category=res.category, message=res.message))
            db.session.commit()
        except:
            flash('Invalid input.')
    return render_template('stroke.html', result=result)

@app.route('/arthritis', methods=['GET','POST'])
def arthritis_route():
    result = None
    if request.method == 'POST':
        try:
            joint_pain = request.form.get('joint_pain') == 'on'
            morning_stiffness = request.form.get('morning_stiffness') == 'on'
            swelling = request.form.get('swelling') == 'on'
            family_history = request.form.get('family_history') == 'on'
            difficulty_moving = request.form.get('difficulty_moving') == 'on'
            res = arthritis_score(joint_pain, morning_stiffness, swelling, family_history, difficulty_moving)
            result = res
            db.session.add(History(test='Arthritis', value=res.value, category=res.category, message=res.message))
            db.session.commit()
        except:
            flash('Invalid input.')
    return render_template('arthritis.html', result=result)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/history')
def history_route():
    records = History.query.order_by(History.date.desc()).all()
    return render_template('history.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
