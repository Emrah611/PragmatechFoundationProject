from medical import app,db
import os
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from medical.models import Patient,Profession

#ADMIN
@app.route("/admin-patient-list")
def patient_list():
    patients = Patient.query.all()
    return render_template("admin/patient-list.html",patients=patients)

@app.route("/admin-patient-add", methods=['GET', 'POST'])
def patient_add():
    patient = Patient.query.all()
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        patient = Patient(
            name = request.form['name'],
            surname = request.form['surname'],
            email = request.form['email'],
            date_time = request.form['date-time'],
            description = request.form['description'],
            age = request.form['age'],
            phone = request.form['phone'],
            image = filename,
        )
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('patient_list'))
    return render_template("admin/patient-add.html",patient=patient)


@app.route("/admin-patient-edit/<int:id>", methods=['GET', "POST"])
def patient_edit(id):
    patient = Patient.query.get_or_404(id)
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        patient.name = request.form['name']
        patient.surname = request.form['surname']
        patient.email = request.form['email']
        patient.date_time = request.form['date-time']
        patient.description = request.form['description']
        patient.age = request.form['age']
        patient.phone= request.form['phone']
        patient.image = filename
        db.session.commit()
        return redirect(url_for('patient_list'))
    return render_template('admin/patient-edit.html',patient=patient)


@app.route("/admin-patient-delete/<int:id>")
def patient_delete(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for('patient_list'))

@app.route("/admin-profession", methods=['GET', "POST"])
def profession():
    professions = Profession.query.all()
    if request.method == 'POST':
        profession = Profession(
        specialty = request.form['specialty'],
        description = request.form['description']
        )
        db.session.add(profession)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("admin/profession.html",professions=professions)

@app.route("/admin-profession-edit/<int:id>", methods=['GET', "POST"])
def profession_edit(id):
    profession = Profession.query.get_or_404(id)
    if request.method == 'POST':
        profession.specialty = request.form['specialty']
        profession.description = request.form['description']
        db.session.commit()
        return redirect(url_for('profession'))
    return render_template('admin/profession-edit.html')

@app.route("/admin-profession-delete/<int:id>")
def profession_delete(id):
    profession = Profession.query.get_or_404(id)
    db.session.delete(profession)
    db.session.commit()
    return redirect(url_for('profession_list'))

@app.route("/admin-profession-list")
def profession_list():
    professions = Profession.query.all()
    return render_template("admin/profession-list.html",professions=professions)

#USER 
@app.route('/', methods=['GET', 'POST'])
def home():
    professions = Profession.query.all()
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        patient = Patient(
            name = request.form['name'],
            surname = request.form['surname'],
            email = request.form['email'],
            date_time = request.form['date-time'],
            description = request.form['description'],
            age = request.form['age'],
            phone = request.form['phone'],
            image = filename,
        )
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('patient_list'))
    return render_template('med1.html',professions=professions)

@app.route('/medical')
def medical():
    return render_template('med2.html')

@app.route("/randevu", methods=['GET', 'POST'])
def randevu():
    patients = Patient.query.all()
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        patient = Patient(
            name = request.form['name'],
            surname = request.form['surname'],
            email = request.form['email'],
            date_time = request.form['date-time'],
            description = request.form['description'],
            age = request.form['age'],
            phone = request.form['phone'],
            image = filename,
        )
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('patient_list'))
    return render_template("randevu.html",patients=patients)
