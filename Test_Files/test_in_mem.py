# File: test_in_memory.py
import sys
import os

# Add the directory containing your module to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from in_memory_db import InMemoryDB

def main():
    db = InMemoryDB()

    # Should return 'Key not found', because 'X' doesn't exist yet
    print(db.get('X'))  # Output: Key not found

    try:
        # Should raise an exception because there's no active transaction
        db.put('X', 10)
    except Exception as e:
        print(e)  # Output: No transaction in progress. Please begin a transaction first.

    # Start a transaction
    db.begin_transaction()

    # Put 'X' within the transaction
    db.put('X', 10)

    # Should still return 10, because 'X' is not committed yet but visible within the transaction
    print(db.get('X'))  # Output: 10

    # Commit the transaction
    db.commit()

    # Now 'X' should return 10
    print(db.get('X'))  # Output: 10

    # Try to commit again without an active transaction
    try:
        db.commit()
    except Exception as e:
        print(e)  # Output: No transaction in progress to commit.

    # Start another transaction and rollback
    db.begin_transaction()
    db.put('X', 20)
    print(db.get('X'))  # Output: 20
    db.rollback()
    print(db.get('X'))  # Output: 10

if __name__ == "__main__":
    main()
