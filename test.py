import unittest
from app import app
from models import db, Bank, Branch

class APITestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            # Explicitly drop all tables to ensure a clean state for each test
            db.drop_all()
            db.create_all()
            # Populate with a small amount of test data
            bank = Bank(id=1, name="TEST BANK")
            branch = Branch(ifsc="TEST0001234", bank_id=1, branch="TEST BRANCH", address="TEST ADDRESS", city="TEST CITY", district="TEST DISTRICT", state="TEST STATE")
            db.session.add(bank)
            db.session.add(branch)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_banks(self):
        """Test getting the list of all banks."""
        response = self.app.get('/banks')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'TEST BANK')

    def test_get_branch_details(self):
        """Test getting a specific branch by IFSC code."""
        response = self.app.get('/branches/TEST0001234')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['ifsc'], 'TEST0001234')
        self.assertEqual(data['bank_name'], 'TEST BANK')

    def test_get_branch_not_found(self):
        """Test getting a branch that does not exist."""
        response = self.app.get('/branches/NONEXISTENT')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['error'], 'Branch not found')

if __name__ == '__main__':
    unittest.main()