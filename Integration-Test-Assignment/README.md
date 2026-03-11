# Integration Testing Assignment

## Overview

This repository demonstrates **integration testing in Python** using the `pytest` framework.
Integration testing ensures that different components or modules of an application interact correctly when combined.

In this assignment, a simple system consisting of a **Database module** and a **Service module** is created. Integration tests are written to validate the interaction between these components.


---
## Components

### 1. Database Module (`database.py`)

This module simulates a simple database using a dictionary.

Functions:

* Store user data
* Retrieve user information based on user ID

---

### 2. Service Module (`service.py`)

This module interacts with the database module.

Responsibilities:

* Request user data from the database
* Return appropriate responses based on whether the user exists

---

### 3. Integration Tests (`test_integration.py`)

Integration tests verify that the **Service module correctly interacts with the Database module**.

Test cases implemented:

* Validate retrieval of an existing user
* Validate response when a user does not exist

These tests ensure that multiple components of the system work correctly together.

---

## Technologies Used

* Python 3
* pytest
* GitHub

---

## Running the Tests

Install pytest:

```
pip install pytest
```

Run the tests:

```
pytest
```

Expected output:

```
2 passed in 0.02s
```

---

## Learning Outcomes

Through this assignment, the following concepts were practiced:

* Understanding integration testing
* Testing interaction between multiple modules
* Using pytest for automated testing
* Structuring Python testing projects

---

## Author

**Nirmalya Das**
