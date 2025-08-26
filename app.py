import os
from flask import Flask, jsonify
from models import db, Bank, Branch
from database import init_db

app = Flask(__name__)

# Use DATABASE_URL from Render environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create tables if they don't exist
with app.app_context():
    init_db(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Bank API! 🏦"})

@app.route('/banks', methods=['GET'])
def get_banks():
    banks = Bank.query.all()
    return jsonify([{"id": b.id, "name": b.name} for b in banks])

@app.route('/branches/<string:ifsc>', methods=['GET'])
def get_branch_details(ifsc):
    branch = Branch.query.filter_by(ifsc=ifsc).first()
    if branch:
        bank = Bank.query.get(branch.bank_id)
        return jsonify({
            "ifsc": branch.ifsc,
            "bank_name": bank.name,
            "branch": branch.branch,
            "address": branch.address,
            "city": branch.city,
            "district": branch.district,
            "state": branch.state
        })
    return jsonify({"error": "Branch not found"}), 404
