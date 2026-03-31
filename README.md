# Library Management System with AI Recommendations
## Student Details
Name: Yogesh KUMAR
Registration Number: 25BAI10227
Course: B.Tech CSE (AIML)
## Project Overview
The Library Management System is a Python-based console application designed to
automate the daily operations of a library. It efficiently manages two main databases:
Books and Members.
This project highlights the use of the Pandas library for structured data display and
an **AI Recommendation Engine** that suggests books based on users' reading
history and preferred genres.
## Key Features
- Dual Database Management: Separate modules for Books and Members
- CRUD Operations: Add, Display, Search, Modify, and Delete records
- Smart Issue System: Manages book issuing, return, and availability status
- AI Recommendation Engine: Uses `collections.Counter` to suggest books based on
most-read genres
- Tabular Data Display: Uses Pandas for clean and professional table format
- Input Validation: Handles errors using try-except blocks
## Technical Stack
- Language: Python 3.13
- Libraries:
- pandas (for structured data and display)
- collections.Counter (for AI recommendations)
- Data Storage: Nested Dictionaries for fast operations
## System Logic
- Books Dictionary:
`{BID: [Title, Author, Publisher, Edition, Genre, Price, Status]}`
- Members Dictionary:
`{MID: [Name, DOB, Contact, Address, Books Issued, DOJ, MED, Status]}`
- Issued Dictionary:
Maps Member IDs to issued Book IDs
## How to Run
1. Ensure Python 3.13 is installed
2. Install required library:
bash
pip install pandas
