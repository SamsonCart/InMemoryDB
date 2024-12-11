class InMemoryDB:
    def __init__(self):
        self.data = {}
        self.transaction = False
        self.temp_data = {}

    def begin_transaction(self):
        if not self.transaction:
            self.transaction = True
            self.temp_data = self.data.copy()
            return "Transaction started."
        else:
            return "Transaction already in progress."

    def put(self, key, value):
        if self.transaction:
            self.temp_data[key] = value
            return f"Key '{key}' updated to {value}."
        else:
            raise Exception("No transaction in progress. Please begin a transaction first.")

    def get(self, key):
        if self.transaction and key in self.temp_data:
            return self.temp_data[key]
        elif key in self.data:
            return self.data[key]
        else:
            return "Key not found."

    def commit(self):
        if self.transaction:
            self.data = self.temp_data.copy()
            self.transaction = False
            return "Transaction committed."
        else:
            raise Exception("No transaction in progress to commit.")

    def rollback(self):
        if self.transaction:
            self.temp_data = self.data.copy()
            self.transaction = False
            return "Transaction rolled back."
        else:
            raise Exception("No transaction in progress to rollback.")

def main():
    db = InMemoryDB()
    print("\nWelcome to the In-Memory Database CLI!\n")
    print("Remember, you must start a transaction before performing other operations.\n")
    while True:
        print("----------------------------------------------------------")
        print("Choose an option by entering the corresponding number:\n")
        print("1. Begin Transaction")
        print("2. Put (Add/Update Key-Value Pair)")
        print("3. Get (Retrieve Value by Key)")
        print("4. Commit Transaction")
        print("5. Rollback Transaction")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()
        try:
            if choice == "1":
                print(db.begin_transaction())
            elif choice == "2":
                key = input("Enter key: ").strip()
                value = input("Enter value (integer): ").strip()
                print(db.put(key, int(value)))
            elif choice == "3":
                key = input("Enter key: ").strip()
                print(db.get(key))
            elif choice == "4":
                print(db.commit())
            elif choice == "5":
                print(db.rollback())
            elif choice == "6":
                print("Exiting CLI. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
