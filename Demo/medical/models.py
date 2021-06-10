from medical import db
from datetime import datetime

class Patient(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String, unique=True)
    date_time = db.Column(db.String(100),default=datetime.now)
    description = db.Column(db.Text(80),nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.Text(80),nullable=False)
    image = db.Column(db.String(20), default='uploads/images.jpg')

    def __repr__(self):
        return f'Patient {self.name}'

class Profession(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    specialty = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(30),nullable=False)

    def __repr__(self):
        return f'Profession {self.specialty}'