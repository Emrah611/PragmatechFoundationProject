from medical import app,db
import os
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from medical.models import Patient,Profession,Doctor,Comment,Service,Update,Addcomment,Department,Note,Blog


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
    professions = Profession.query.get_or_404(id)
    if request.method == 'POST':
        professions.specialty = request.form['specialty']
        professions.description = request.form['description']
        db.session.commit()
        return redirect(url_for('profession_list'))
    return render_template('admin/profession-edit.html',professions=professions)

@app.route("/admin-profession-delete/<int:id>")
def profession_delete(id):
    professions = Profession.query.get_or_404(id)
    db.session.delete(professions)
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
        doctors.name = request.form['name']
        doctors.specialty = request.form['specialty']
        doctors.description = request.form['description']
        doctors.image = filename
        db.session.commit()
        return redirect(url_for('doctor_list'))
    return render_template('admin/doctor-edit.html',doctors=doctors)

@app.route("/admin-doctor-delete/<int:id>")
def doctor_delete(id):
    doctors = Doctor.query.get_or_404(id)
    db.session.delete(doctors)
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
        return redirect(url_for('comment_list'))
    return render_template('admin/comment-edit.html',comments=comments)

@app.route("/admin-comment-delete/<int:id>")
def comment_delete(id):
    comments = Comment.query.get_or_404(id)
    db.session.delete(comments)
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
        return redirect(url_for('service_list'))
    return render_template('admin/service-edit.html',services=services)

@app.route("/admin-service-delete/<int:id>")
def service_delete(id):
    services = Service.query.get_or_404(id)
    db.session.delete(services)
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
    updates = Update.query.get_or_404(id)
    db.session.delete(updates)
    db.session.commit()
    return redirect(url_for('update_list'))

@app.route("/admin-department-add", methods=['GET', 'POST'])
def department_add():
    departments = Department.query.all()
    if request.method == 'POST':
        department = Department(
            title = request.form['title'],
        )
        db.session.add(department)
        db.session.commit()
        return redirect(url_for('department_list'))
    return render_template("admin/department-add.html",departments=departments)


@app.route("/admin-department-list")
def department_list():
    departments = Department.query.all()
    return render_template("admin/department-list.html",departments=departments)


@app.route("/admin-department-edit/<int:id>", methods=['GET', "POST"])
def department_edit(id):
    departments = Department.query.get_or_404(id)
    if request.method == 'POST':
        departments.title = request.form['title']
        db.session.commit()
        return redirect(url_for('department_list'))
    return render_template('admin/department-edit.html',departments=departments)

@app.route("/admin-department-delete/<int:id>")
def department_delete(id):
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    return redirect(url_for('department_list'))

@app.route("/admin-note-add", methods=['GET', 'POST'])
def note_add():
    notes = Note.query.all()
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        note = Note(
            short_description = request.form['short-description'],
            description = request.form['description'],
            description2 = request.form['description2'],
            short_description2 = request.form['short-description2'],
            description3 = request.form['description3'],
            description4 = request.form['description4'],
            image = filename,
        )
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('note_list'))
    return render_template("admin/note-add.html",notes=notes)


@app.route("/admin-note-list")
def note_list():
    notes = Note.query.all()
    return render_template("admin/note-list.html",notes=notes)


@app.route("/admin-note-edit/<int:id>", methods=['GET', "POST"])
def note_edit(id):
    notes = Note.query.get_or_404(id)
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        notes.short_description = request.form['short-description']
        notes.description = request.form['description']
        notes.description2 = request.form['description2']
        notes.short_description2 = request.form['short-description2']
        notes.description3 = request.form['description3']
        notes.description4 = request.form['description4']
        notes.image = filename
        db.session.commit()
        return redirect(url_for('note_list'))
    return render_template('admin/note-edit.html',notes=notes)


@app.route("/admin-note-delete/<int:id>")
def note_delete(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('note_list'))

@app.route("/admin-blog-list")
def blog_list():
    blogs = Blog.query.all()
    return render_template("admin/blog-list.html",blogs=blogs)

@app.route("/admin-blog-add", methods=['GET', 'POST'])
def blog_add():
    blogs = Blog.query.all()
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blog = Blog(
            date_time = request.form['date-time'],
            short_description = request.form['short-description'],
            image = filename,
        )
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('blog_list'))
    return render_template("admin/blog-add.html",blogs=blogs)


@app.route("/admin-blog-edit/<int:id>", methods=['GET', "POST"])
def blog_edit(id):
    blogs = Blog.query.get_or_404(id)
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blogs.date_time = request.form['date-time']
        blogs.short_description = request.form['short-description']
        blogs.image = filename
        db.session.commit()
        return redirect(url_for('blog_list'))
    return render_template('admin/blog-edit.html',blogs=blogs)


@app.route("/admin-blog-delete/<int:id>")
def blog_delete(id):
    blogs = Blog.query.get_or_404(id)
    db.session.delete(blogs)
    db.session.commit()
    return redirect(url_for('blog_list'))


#USER 
@app.route('/', methods=['GET', 'POST'])
def home():
    doctors = Doctor.query.all()
    professions = Profession.query.all()
    comments = Comment.query.all()
    services = Service.query.all()
    updates = Update.query.all()
    addcomments = Addcomment.query.all()
    departments = Department.query.all()
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
        db.session.add(addcomment)
        db.session.commit()
        return redirect(url_for('patient_list'))
    return render_template('med1.html',professions=professions,doctors=doctors,comments=comments,services=services,updates=updates,addcomments=addcomments,departments=departments)

@app.route('/admin-1', methods=['GET', 'POST'])
def admin_med1():
    doctors = Doctor.query.all()
    professions = Profession.query.all()
    comments = Comment.query.all()
    services = Service.query.all()
    updates = Update.query.all()
    addcomments = Addcomment.query.all()
    departments = Department.query.all()
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
        db.session.add(addcomment)
        db.session.commit()
        return redirect(url_for('patient_list'))
    return render_template('admin-med1.html',professions=professions,doctors=doctors,comments=comments,services=services,updates=updates,addcomments=addcomments,departments=departments)



@app.route('/medical', methods=['GET', 'POST'])
def medical():
    addcomments = Addcomment.query.all()
    departments = Department.query.all()
    notes = Note.query.all()
    blogs = Blog.query.all()
    if request.method == 'POST':
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        addcomment = Addcomment(
            name = request.form['user-name'],
            description = request.form['user-description'],
            date_time = request.form['user-datetime'],
            image = filename,
        )
        db.session.add(addcomment)
        db.session.commit()
        return redirect(url_for('medical'))
    return render_template('med2.html',addcomments=addcomments,departments=departments,notes=notes,blogs=blogs)


@app.route('/admin-2', methods=['GET', 'POST'])
def admin_med2():
    addcomments = Addcomment.query.all()
    departments = Department.query.all()
    notes = Note.query.all()
    blogs = Blog.query.all()
    if request.method == 'POST':
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        addcomment = Addcomment(
            name = request.form['user-name'],
            description = request.form['user-description'],
            date_time = request.form['user-datetime'],
            image = filename,
        )
        db.session.add(addcomment)
        db.session.commit()
        return redirect(url_for('medical'))
    return render_template('admin-med2.html',addcomments=addcomments,departments=departments,notes=notes,blogs=blogs)

@app.route("/user-addcomment-list")
def addcomment_list():
    addcomments = Addcomment.query.all()
    return render_template("admin/addcomment-list.html",addcomments=addcomments)

@app.route("/user-addcomment-delete/<int:id>")
def addcomment_delete(id):
    addcomment = Addcomment.query.get_or_404(id)
    db.session.delete(addcomment)
    db.session.commit()
    return redirect(url_for('addcomment_list'))

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
        return redirect(url_for('home'))
    return render_template("randevu.html",patients=patients)