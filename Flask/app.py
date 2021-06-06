from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os.path import join, dirname, realpath, os
from sqlalchemy.orm import backref
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
# from image_upload import save_picture


class Customer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String, unique=True)
    image = db.Column(db.String(20), default='customer.jpeg')
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Customer {self.name}'

@app.route('/admin/customer', methods=['GET', 'POST'])
def customer_add():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        customer = Customer(
            name = request.form['name'],
            email = request.form['email'],
            age = request.form['age'],
            image = filename,
        )
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for('customer_edit'))
    return render_template('admin/customer-add.html')

@app.route("/admin")
def admin():
    return render_template("admin/admin.html")

@app.route('/admin/customer-edit') 
def customer_edit():
    customers = Customer.query.all()
    return render_template('admin/customer-edit.html', customers=customers)

@app.route('/')
def home():
    return render_template('med1.html')

@app.route('/medical')
def medical():
    return render_template('med2.html')



if __name__ == '__main__':
    app.run(debug=True)