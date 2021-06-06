from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os.path import join, dirname, realpath, os
from sqlalchemy.orm import backref
from werkzeug.utils import secure_filename
from datetime import datetime
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)
# from image_upload import save_picture


@app.route("/admin-patient-list")
def patient_list():
    patients = Patient.query.all()
    return render_template("admin/patient-list.html",patients=patients)

@app.route("/admin-patient-add", methods=['GET', 'POST'])
def patient_add():
    categories = PatientCategory.query.all()
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        patient = Patient(
            name = request.form['name'],
            surname = request.form['surname'],
            email = request.form['email'],
            date_time = request.form['date-time'],
            short_description = request.form['short-description'],
            description = request.form['description'],
            age = request.form['age'],
            image = filename,
        )
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('patient_list'))
    return render_template("admin/patient-add.html",categories=categories)


@app.route("/admin-patient-edit/<int:id>", methods=['GET', "POST"])
def patient_edit(id):
    patient = Patient.query.get_or_404(id)
    categories = PatientCategory.query.all()
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        patient.name = request.form['name']
        patient.surname = request.form['surname']
        patient.email = request.form['email']
        patient.date_time = request.form['date-time']
        patient.short_description = request.form['short-description']
        patient.description = request.form['description']
        patient.age = request.form['age']
        patient.image = filename
        db.session.commit()
        return redirect(url_for('patient_list'))
    return render_template('admin/patient-edit.html', categories=categories)


@app.route("/admin-patient-delete/<int:id>")
def patient_delete(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for('patient_list'))



class Patient(db.Model):

    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String, unique=True)
    date_time = db.Column(db.String(100),default=datetime.now)
    short_description = db.Column(db.String(100),nullable = False)
    description = db.Column(db.Text(80),nullable=False)
    image = db.Column(db.String(20), default='uploads/images.jpg')
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Patient {self.name}'

class PatientCategory(db.Model):
    __tablename__ = 'patientcategory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'Category {self.name}'


#USER 
@app.route('/')
def home():
    return render_template('med1.html')

@app.route('/medical')
def medical():
    return render_template('med2.html')

@app.route("/randevu", methods=['GET', 'POST'])
def randevu():
    categories = PatientCategory.query.all()
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        patient = Patient(
            name = request.form['name'],
            surname = request.form['surname'],
            email = request.form['email'],
            date_time = request.form['date-time'],
            short_description = request.form['short-description'],
            description = request.form['description'],
            age = request.form['age'],
            image = filename,
        )
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('patient_list'))
    return render_template("randevu.html",categories=categories)


if __name__ == '__main__':
    app.run(debug=True)






















# @app.route("/admin")
# def admin():
#     return render_template("admin/admin.html")

# @app.route('/admin/patient-edit') 
# def patient_edit():
#     patients = patient.query.all()
#     return render_template('admin/patient-edit.html', patients=patients)


