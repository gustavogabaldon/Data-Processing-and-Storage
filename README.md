# Data-Processing-and-Storage

# In-Memory Key-Value Database with Transactions

## Overview
This project provides an in-memory key-value database that supports transactional operations. You can begin a transaction, put keys and values during that transaction, and then either commit (making changes permanent) or rollback (getting rid of all changes made). This is especially useful in scenarios where preciseness of operations is crucial, like financial transactions.

You can:

- Begin a transaction (begin_transaction())
- Put key-value pairs (put(key, value)) within the transaction
- Retrieve values with get(key) at any time
- Commit a transaction (commit()) to make all changes permanent
- Rollback a transaction (rollback()) to discard any uncommitted changes
This approach simulates precise operations similar to those needed in financial transactions. For example, if you are building a money-transfer feature and one step of updating account balances fails, a rollback ensures the system returns to a stable previous state, preventing inconsistencies in data.

Features and Requirements
- Keys are strings.
- Values are integers.
- If put(key, val) is called without an active transaction, the code raises an exception.
- get(key) returns the value if it exists in committed state or the currently active transaction’s state; otherwise, it returns None.
- Only one transaction may be active at any time.
- Uncommitted changes (made within a transaction) are not visible to get() calls outside that transaction until committed.
- commit() makes all transaction changes permanent.
- rollback() discards all changes made within the current transaction.

## How to Run
1. Ensure you have Python 3 installed.
2. Clone the repository:  
   ```bash
   git clone https://github.com/gustavogabaldon/Data-Processing-and-Storage.git
   cd Data-Processing-and-Storage
3. Run the code: python transactional_inmemory_db.py

## Future Assignment Improvements

- Add more robust error handling for edge cases
- Implement nested transaction support
- Add persistent storage option
- Create more comprehensive test cases covering complex scenarios
- Add type hinting and more detailed documentation for each method


