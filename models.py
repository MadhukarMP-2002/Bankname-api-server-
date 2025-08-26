from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bank(db.Model):
    __tablename__ = 'banks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    branches = db.relationship('Branch', backref='bank', lazy=True)

class Branch(db.Model):
    __tablename__ = 'branches'
    ifsc = db.Column(db.String(11), primary_key=True)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'), nullable=False)
    branch = db.Column(db.String(255))
    address = db.Column(db.String(255))
    city = db.Column(db.String(255))
    district = db.Column(db.String(255))
    state = db.Column(db.String(255))