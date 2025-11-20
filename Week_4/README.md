# Python Practice Tasks – Week 4

This folder contains my Python exercises for Week 4. Each task focuses on specific programming concepts, helping me improve problem-solving skills and Python knowledge.

## Tasks Included

1. **Bank Account System (Class + Dunder Methods)**
   - Create a `BankAccount` class to manage account information and transactions.
   - `__init__`: Initialize account number, balance, type (savings/checking), and opening date (`datetime`).
   - `__str__`: Returns account information in readable format.
   - `__add__`: Combine balances of two accounts.
   - `deposit` & `withdraw`: Methods for adding and withdrawing money; `withdraw` checks sufficient balance.
   - `account_report`: Show transaction history with timestamps.
   - Demonstrates **OOP**, **dunder methods**, and **datetime usage**.

2. **Student Grading System (Inheritance + Collections)**
   - Implement a grading system using inheritance.
   - `Student` base class: name, surname, student ID, and grades dictionary.
   - `add_grade`: Add grades to courses, track statistics with `collections.Counter`.
   - `calculate_average`: Round averages using `math.ceil` or `math.floor`.
   - `UndergraduateStudent`: Weighted average formula (e.g., 40% midterm, 60% final).
   - `GraduateStudent`: Different grading criteria.
   - Demonstrates **inheritance**, **collections**, and **math module**.

3. **File Manager (File Operations + Random)**
   - Build a file and folder management system.
   - `create_file`: Randomly generate file names using `random`.
   - `read_file_regex`: Search patterns in files using `re`.
   - `scan_folder`: List all files in a folder using `os`.
   - `__len__`: Return number of files in a folder.
   - `backup_file`: Create a backup copy of a file.
   - Demonstrates **file handling**, **regex**, **os module**, and **random**.

4. **E-Commerce System (OOP Composition)**
   - Develop a system with products, customers, and orders.
   - `Product` class: name, price, stock (property decorator), barcode (randomly generated).
   - `Customer` class: name, email, shopping cart, order history.
   - `Order` class: order number (random), date (`datetime`), total price.
   - `make_payment`: Calculate total including VAT (18%) using `math`.
   - `update_stock`: Update stock after purchase.
   - `__contains__`: Check if a product is in the customer's cart.
   - Demonstrates **composition**, **OOP**, and **math module usage**.

5. **Quiz Application (Collections + Random)**
   - Build a timed quiz application with random questions and detailed reports.
   - `question_bank`: Dictionary with question, answer, difficulty level.
   - `select_questions`: Randomly select a number of questions using `random.sample`.
   - `start_quiz`: Start timer using `time.time`.
   - `check_answers`: Track correct/incorrect answers using `collections.Counter`.
   - `generate_report`: Create detailed report with timestamps using `datetime`.
   - `calculate_score`: Compute score with difficulty multiplier using `math`.
   - Demonstrates **random selection**, **collections**, **time handling**, and **scoring logic**.

6. **Employee Management System (Advanced OOP)**
   - Manage company personnel with inheritance and advanced OOP features.
   - `Employee` base class: name, surname, salary, department, start date (`datetime`).
   - `calculate_raise`: Determine raise percentage based on tenure.
   - `calculate_leave`: Compute leave days using `datetime.timedelta`.
   - `Manager` subclass: Track team members, calculate bonuses.
   - `Developer` subclass: Track technology stack, calculate project-based bonuses.
   - `__eq__`: Compare salaries between employees.
   - `__gt__`: Compare tenure between employees.
   - Demonstrates **advanced OOP**, **inheritance**, **datetime**, and **operator overloading**.

## How to Run

- Each task is independent.  
- Open the Python file for each task and run it in your preferred environment (PyCharm, VS Code, etc.).  
- Follow on-screen prompts for input where applicable.
