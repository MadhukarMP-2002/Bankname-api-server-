import csv
import os
from models import db, Bank, Branch

def init_db(app_instance):
    with app_instance.app_context():
        db.create_all()
        populate_db()

def populate_db():
    if Branch.query.first():
        print("Database already populated. Skipping...")
        return

    bank_map = {}
    bank_id_counter = 1

    csv_path = os.path.join(os.path.dirname(__file__), "bank_branches.csv")
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            bank_name = row['bank_name']
            if bank_name not in bank_map:
                bank_map[bank_name] = bank_id_counter
                bank = Bank(id=bank_id_counter, name=bank_name)
                db.session.add(bank)
                bank_id_counter += 1

            bank_id = bank_map[bank_name]
            branch = Branch(
                ifsc=row['ifsc'],
                bank_id=bank_id,
                branch=row['branch'],
                address=row['address'],
                city=row['city'],
                district=row['district'],
                state=row['state']
            )
            db.session.add(branch)

    db.session.commit()
    print("Database populated successfully.")
