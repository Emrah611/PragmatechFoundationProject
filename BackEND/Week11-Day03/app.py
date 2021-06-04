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
    orders = db.relationship('Order', backref='owner', lazy=True)

    def __repr__(self):
        return f'Customer {self.name}'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    short_description = db.Column(db.String(127), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), default='image.png')
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    def __repr__(self):
        return f'Order {self.title}'


@app.route('/admin/add-customer', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        customer = Customer(
            name = request.form['name'], # Ali
            email = request.form['email'],
            age = request.form['age'],
            image = filename,
        )
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for('edit_customer'))
    return render_template('admin/card-add.html')

@app.route('/admin/edit-customer')
def edit_customer():
    customers = Customer.query.all()
    return render_template('admin/card-edit.html', customers=customers)
    
@app.route('/customer-list')
def customers():
    customers = Customer.query.all()
    return render_template('index.html', customers=customers)

if __name__ == '__main__':
    app.run(debug=True)