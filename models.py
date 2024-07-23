from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Human(db.Model):
    __tablename__ = 'human'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'human',
        'polymorphic_on': type
    }

class Student(Human):
    __tablename__ = 'student'
    id = db.Column(db.Integer, db.ForeignKey('human.id'), primary_key=True)
    student_id = db.Column(db.Integer, unique=True)
    year = db.Column(db.String(100), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'student',
    }

class Doctor(Human):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer, db.ForeignKey('human.id'), primary_key=True)
    doctor_id = db.Column(db.Integer, unique=True)
    year = db.Column(db.String(100), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'doctor',
    }
