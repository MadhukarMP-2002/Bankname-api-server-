import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from models import db, Bank, Branch
from database import init_db

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ✅ Ensure tables are created, works under Flask & Gunicorn
with app.app_context():
    init_db(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Bank API! 🏦"})

@app.route('/banks', methods=['GET'])
def get_banks():
    banks = Bank.query.all()
    bank_list = [{"id": b.id, "name": b.name} for b in banks]
    return jsonify(bank_list)

@app.route('/branches/<string:ifsc>', methods=['GET'])
def get_branch_details(ifsc):
    branch = Branch.query.filter_by(ifsc=ifsc).first()
    if branch:
        bank = Bank.query.get(branch.bank_id)
        branch_details = {
            "ifsc": branch.ifsc,
            "bank_name": bank.name,
            "branch": branch.branch,
            "address": branch.address,
            "city": branch.city,
            "district": branch.district,
            "state": branch.state
        }
        return jsonify(branch_details)
    return jsonify({"error": "Branch not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
