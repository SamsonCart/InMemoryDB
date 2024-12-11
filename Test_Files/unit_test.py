# File: test_unit.py
import sys
import os

# Add the directory containing your module to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from in_memory_db import InMemoryDB

class TestInMemoryDB(unittest.TestCase):
    def test_get_nonexistent_key(self):
        db = InMemoryDB()
        self.assertEqual(db.get("Y"), "Key not found")

    def test_put_without_transaction(self):
        db = InMemoryDB()
        with self.assertRaises(Exception) as context:
            db.put('Y', 25)
        self.assertTrue('No transaction in progress. Please begin a transaction first.' in str(context.exception))

    def test_transactional_operations(self):
        db = InMemoryDB()

        db.begin_transaction()
        db.put("Y", 25)
        self.assertEqual(db.get("Y"), 25)  # Should see the uncommitted change

        db.commit()
        self.assertEqual(db.get("Y"), 25)  # After commit, should still see 25

        db.begin_transaction()
        db.put("Y", 30)
        self.assertEqual(db.get("Y"), 30)  # Updated in transaction but not yet committed
        db.rollback()
        self.assertEqual(db.get("Y"), 25)  # After rollback, should revert to 25

    def test_rollback_without_transaction(self):
        db = InMemoryDB()
        with self.assertRaises(Exception) as context:
            db.rollback()
        self.assertTrue("No transaction in progress to rollback." in str(context.exception))

if __name__ == '__main__':
    unittest.main()
