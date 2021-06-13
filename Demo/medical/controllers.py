from medical import app,db
import os
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from medical.models import Patient,Profession,Doctor,Comment,Service,Update


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
    return render_template('admin/profession-edit.html',professions=professions)

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


@app.route('/admin-doctor-add', methods=['GET', 'POST'])
def doctor_add():
    doctors = Doctor.query.all()
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        doctor = Doctor(
            name = request.form['name'],
            specialty = request.form['specialty'],
            description = request.form['description'],
            image = filename,
        )
        db.session.add(doctor)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('admin/doctor-add.html',doctors=doctors)

@app.route("/admin-doctor-edit/<int:id>", methods=['GET', "POST"])
def doctor_edit(id):
    doctors = Doctor.query.get_or_404(id)
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        doctor.name = request.form['name']
        doctor.specialty = request.form['specialty']
        doctor.description = request.form['description']
        doctor.image = filename
        db.session.commit()
        return redirect(url_for('doctor_add'))
    return render_template('admin/doctor-edit.html',doctors=doctors)

@app.route("/admin-doctor-delete/<int:id>")
def doctor_delete(id):
    doctors = Doctor.query.get_or_404(id)
    db.session.delete(doctor)
    db.session.commit()
    return redirect(url_for('doctor_list'))

@app.route("/admin-doctor-list")
def doctor_list():
    doctors = Doctor.query.all()
    return render_template("admin/doctor-list.html",doctors=doctors)

@app.route('/admin-comment-add', methods=['GET', 'POST'])
def comment_add():
    comments = Comment.query.all()
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        comment = Comment(
            full_name = request.form['full_name'],
            description = request.form['description'],
            image = filename,
        )
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('admin/comment-add.html',comments=comments)

@app.route("/admin-comment-list")
def comment_list():
    comments = Comment.query.all()
    return render_template("admin/comment-list.html",comments=comments)

@app.route("/admin-comment-edit/<int:id>", methods=['GET', "POST"])
def comment_edit(id):
    comments = Comment.query.get_or_404(id)
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        comments.full_name = request.form['full_name']
        comments.description = request.form['description']
        comments.image = filename
        db.session.commit()
        return redirect(url_for('comment_add'))
    return render_template('admin/comment-edit.html',comments=comments)

@app.route("/admin-comment-delete/<int:id>")
def comment_delete(id):
    comments = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('comment_list'))

@app.route('/admin-service-add', methods=['GET', 'POST'])
def service_add():
    services = Service.query.all()
    if request.method == 'POST':
        service = Service(
            service = request.form['services'],
            description = request.form['description'],
        )
        db.session.add(service)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('admin/service-add.html',services=services)

@app.route("/admin-service-list")
def service_list():
    services = Service.query.all()
    return render_template("admin/service-list.html",services=services)

@app.route("/admin-service-edit/<int:id>", methods=['GET', "POST"])
def service_edit(id):
    services = Service.query.get_or_404(id)
    if request.method == 'POST':
        services.services = request.form['services']
        services.description = request.form['description']
        db.session.commit()
        return redirect(url_for('service_add'))
    return render_template('admin/service-edit.html',services=services)

@app.route("/admin-service-delete/<int:id>")
def service_delete(id):
    service = Service.query.get_or_404(id)
    db.session.delete(service)
    db.session.commit()
    return redirect(url_for('service_list'))


@app.route("/admin-update-list")
def update_list():
    updates = Update.query.all()
    return render_template("admin/update-list.html",updates=updates)

@app.route("/admin-update-add", methods=['GET', 'POST'])
def update_add():
    updates = Update.query.all()
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        update = Update(
            date_time = request.form['date-time'],
            description = request.form['description'],
            short_description = request.form['short-description'],
            image = filename,
        )
        db.session.add(update)
        db.session.commit()
        return redirect(url_for('update_list'))
    return render_template("admin/update-add.html",updates=updates)


@app.route("/admin-update-edit/<int:id>", methods=['GET', "POST"])
def update_edit(id):
    updates = Update.query.get_or_404(id)
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        updates.date_time = request.form['date-time']
        updates.description = request.form['description']
        updates.short_description = request.form['short-description']
        updates.image = filename
        db.session.commit()
        return redirect(url_for('update_list'))
    return render_template('admin/update-edit.html',updates=updates)


@app.route("/admin-update-delete/<int:id>")
def update_delete(id):
    update = Update.query.get_or_404(id)
    db.session.delete(update)
    db.session.commit()
    return redirect(url_for('update_list'))



#USER 
@app.route('/', methods=['GET', 'POST'])
def home():
    doctors = Doctor.query.all()
    professions = Profession.query.all()
    comments = Comment.query.all()
    services = Service.query.all()
    updates = Update.query.all()
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
    return render_template('med1.html',professions=professions,doctors=doctors,comments=comments,services=services,updates=updates)


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
