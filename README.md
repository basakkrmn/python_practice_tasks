# Python Practice Tasks

This repository contains my step-by-step Python learning exercises.  
The tasks are organized by week, and each task focuses on a specific programming concept to improve my problem-solving skills and Python proficiency.

## Week Structure

- **Week 1:** Basic Python concepts and simple applications
- **Week 2:** Intermediate Python exercises with loops, conditionals, and built-in functions
- **Week 3:** Advanced Python exercises with generators, recursion, lambda, map/filter, and real-time data processing
- **Week 4:** Advanced OOP, Class Methods, File Operations, Random, and System Simulations
- **Week 5:** Computer Vision, Image Processing, Video Processing, Motion Tracking, Face Detection, and Augmented Reality with OpenCV
- **Week 6:** Real-time communication with Socket.IO, client-server architecture, broadcasting, rooms, namespaces, and asynchronous networking

## Week 1 Tasks

1. **Student Grade Tracking System** – Store student info, calculate averages, determine pass/fail.
2. **Word Frequency Analyzer** – Count word occurrences in a text, ignoring punctuation and case.
3. **User Registration and Login System** – Validate username, password, email, and age.
4. **Basic Calculator** – Perform addition, subtraction, multiplication, and division with proper handling.
5. **Credit Application Evaluation** – Approve or reject credit based on age and income.
6. **Smart Home Temperature Analysis** – Analyze room temperature comfort, calculate max/min/average, count AC/heating hours.

## Week 2 Tasks

1. **Squares of Numbers** – Create a list of squares for numbers 1 to 10.
2. **Multiplication Table** – Generate a multiplication table from 1 to 10 using nested loops.
3. **Number Guessing Game** – Guess a random number between 1 and 100 with hints and limited attempts.
4. **Sum of Odd Numbers** – Ask the user for 10 numbers and sum only the odd ones.
5. **Zip Function with Index** – Combine two lists and print index, name, and age.
6. **Range Function Practice** – 
   - a) Sum of even numbers from 1 to 100  
   - b) Print numbers from 50 down to 40 in reverse order

## Week 3 Tasks

1. **Fibonacci Series with Generator** – Generate Fibonacci numbers up to a user-defined `n`, filter odd numbers, take square roots of even numbers using lambda and map.
2. **Recursive List Flattening** – Flatten a nested list recursively, keep only numbers, implemented with recursive lambda and map/filter.
3. **Real-Time Data Processing System** – Continuously accept numbers, calculate moving average, standard deviation, and detect anomalies (3-sigma rule) using generators, map/reduce, and lambda.
4. **Square Root Calculator** – Calculate the square root of a user input number with error handling for negative numbers or invalid inputs using try-except.
5. **Four-Function Calculator** – Perform addition, subtraction, multiplication, division with user input, handle division by zero and invalid operations using lambda and try-except.
6. **Name Formatter** – Convert a list of names to uppercase and prepend `"Sayın "` using lambda and map; input accepted as comma-separated names.

## Week 4 Tasks

1. **Bank Account System** – Create BankAccount class with __init__, __str__, __add__ methods, withdrawal/deposit functions, and transaction history reporting.
2. **Student Grading System** – Student base class with Undergraduate and Graduate subclasses, grade management using Counter, and different average calculation methods.
3. **File Manager** – Comprehensive file and folder operations manager with random file naming, regex search, folder scanning, and file counting using __len__.
4. **E-Commerce System** – Product, Customer, and Order management system with stock control, cart management, price calculation with VAT, and order processing.
5. **Quiz Application** – Timed quiz application with random question selection, time tracking, detailed reporting, and score calculation based on difficulty levels.
6. **Employee Management System** – Advanced company personnel management system with inheritance for different employee types, salary raise calculations, leave calculations, and comparison operators.

## Week 5 Tasks

1. **Image Transformations** – Apply resizing, rotation, cropping, and flipping operations using OpenCV.
2. **Edge Detection** – Detect edges in images using Canny and Sobel operators.
3. **Color Detection** – Use HSV masking to isolate and track specific colors.
4. **Face Detection** – Detect faces in images or webcam feed using Haar Cascades.
5. **Shape Detection** – Find contours and classify shapes (triangle, square, circle, etc.).
6. **Augmented Reality Marker System** – Detect markers and overlay virtual images using perspective transform.

## Week 6 Tasks

1. **Basic Socket.IO Server & Client** – Create a server listening on port 5000 and a client that connects to it, exchanging welcome messages upon connection/disconnection.
2. **Sending Custom Events & Data** – Implement a login system where the client sends a dictionary (username, level) and the server responds with a personalized message.
3. **Real-Time Chat (Broadcasting)** – Build a chat system where a message sent by one client is instantly broadcast to all connected clients.
4. **Working with Rooms** – Implement logic for clients to join specific rooms (RoomA, RoomB) and ensure messages are only broadcast within their respective rooms.
5. **Namespaces & Event Separation** – Separate logic using namespaces: `/chat` for messaging and `/status` for system health checks.
6. **Asynchronous Socket.IO Server** – Build a non-blocking server using `aiohttp` and `asyncio` to handle heavy loads and time-based events asynchronously.

## How to Run

- Each task is independent and can be run in any Python environment (PyCharm, VS Code, etc.).
- Navigate to the week folder (`Week_1/`, `Week_2/`, `Week_3/`, `Week_4/`, `Week_5/`, `Week_6/`) and run the Python file for each task.

## Notes

- This repository is a learning diary to track progress in Python.
- Each task helps practice different concepts: loops, conditionals, lists, dictionaries, functions, input/output, built-in Python modules, recursion, generators, lambda, map/filter, real-time data handling, OOP, classes, inheritance, file operations, computer vision, augmented reality, and socket programming.