# In-Memory Database CLI

## Overview

This project implements an in-memory key-value database with transaction support. It allows for the basic operations of a key-value store such as adding, updating, and retrieving values, along with transactional control mechanisms including begin, commit, and rollback operations.

## Features

- **Begin Transaction**: Start a new transaction.
- **Put (Add/Update Key-Value Pair)**: Insert or update values within a transaction.
- **Get (Retrieve Value by Key)**: Fetch the value associated with a specific key.
- **Commit Transaction**: Commit all changes made during the current transaction.
- **Rollback Transaction**: Rollback all changes made during the current transaction.
- **Exit**: Terminate the application.

## Files in the Repository

- `main.py`: Contains the `InMemoryDB` class and CLI for database interactions.
- `unit_test.py`: Unit tests to verify the correctness of the database operations.
- `test_in_mem.py`: Script for basic functionality testing of the database.

## Setup

### Prerequisites

- Python 3.6 or higher

### Running the Application

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the application using the command:

   ```bash
   python main.py

## Testing

To run the unit tests, use the following command from the project directory:

python -m unittest test.unit_test

To run the functional tests, execute:

python test.test_in_mem.py

## How to Use

After starting the application, you will be prompted with a menu to select various operations. Follow the on-screen prompts to begin transactions, add or update keys, retrieve values, commit or rollback transactions, or exit the program.

## Assignment Feedback and Suggestions for Improvement

This assignment provides a solid foundation for understanding basic database operations and transaction management. However, there are several areas where the assignment could be enhanced to improve clarity and learning depth:

- **Instructions Clarification**: More detailed descriptions of expected behaviors for undefined keys and error handling during transactions would aid in consistent implementation across submissions.
- **Feature Complexity**: Incorporating features like concurrency management and savepoints would offer a more realistic and challenging learning experience.
- **Testing Specifications**: Clear requirements for test scenarios, including stress tests and concurrency tests, would ensure comprehensive testing coverage.
- **Grading Criteria**: A more detailed grading rubric, including code style and performance considerations, would provide clearer targets for students to aim for excellence.
- **Extension of Learning Objectives**: Suggesting further developments like networking capabilities or discussions on scalability could provide pathways for continued learning.

## Conclusion

This in-memory database project provides a basic yet powerful example of transactional data management within software applications. It serves as an educational tool for understanding database operations and transactional integrity.



