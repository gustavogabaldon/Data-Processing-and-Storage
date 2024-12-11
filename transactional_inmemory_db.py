class InMemoryDBException(Exception):
    pass

class InMemoryDB:
    def __init__(self):
        self.main_store = {}
        self.transaction_store = {}
        self.in_transaction = False

    def get(self, key: str):
        if self.in_transaction and key in self.transaction_store:
            return self.transaction_store[key]
        return self.main_store.get(key, None)

    def put(self, key: str, val: int):
        if not self.in_transaction:
            raise InMemoryDBException("No transaction in progress. Cannot put key-value.")
        self.transaction_store[key] = val

    def begin_transaction(self):
        if self.in_transaction:
            raise InMemoryDBException("Transaction already in progress.")
        self.in_transaction = True
        self.transaction_store = {}

    def commit(self):
        if not self.in_transaction:
            raise InMemoryDBException("No transaction in progress. Cannot commit.")
        for key, val in self.transaction_store.items():
            self.main_store[key] = val
        self.transaction_store = {}
        self.in_transaction = False

    def rollback(self):
        if not self.in_transaction:
            raise InMemoryDBException("No transaction in progress. Cannot rollback.")
        self.transaction_store = {}
        self.in_transaction = False


if __name__ == "__main__":
    db = InMemoryDB()

    print(db.get("A"))  # expected: None

    try:
        db.put("A", 5)  # should raise exception (no transaction)
    except InMemoryDBException as e:
        print(e)

    db.begin_transaction()
    db.put("A", 5)
    print(db.get("A"))  # expected None, not committed yet
    db.put("A", 6)
    db.commit()
    print(db.get("A"))  # expected 6 after commit

    try:
        db.commit()  # no active transaction
    except InMemoryDBException as e:
        print(e)

    try:
        db.rollback()  # no active transaction
    except InMemoryDBException as e:
        print(e)

    print(db.get("B"))  # expected None
    db.begin_transaction()
    db.put("B", 10)
    db.rollback()
    print(db.get("B"))  # expected None after rollback
