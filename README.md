# Overview

For this project, I made an Expense Tracker using Python and SQLite. The program lets users add expenses, view their expenses, update them, and delete them. Each expense has a name, category, amount, and date. There is also a spending summary that shows the number of expenses, the total amount spent, and the average expense.

To use the program, run `main.py` and choose an option from the menu. The program will ask for the information it needs, and the expenses are saved in a database so they are still there when the program is run again.

I wanted to make this project to get more practice with Python and learn how to connect a program to a relational database. I also wanted to get more comfortable writing SQL commands and using them to work with data.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

I used SQLite for my database. SQLite stores information in tables, and I used Python's built-in `sqlite3` library to connect my program to the database.

My database has one table called `expenses`. It contains these columns:

- `id`: A unique ID for each expense that is automatically generated.
- `name`: The name of the expense.
- `category`: The category the expense belongs to.
- `amount`: How much the expense cost.
- `date`: The date of the expense, stored in YYYY-MM-DD format.

The program uses SQL commands to add, view, update, and delete expenses. It also uses `COUNT`, `SUM`, and `AVG` to calculate information for the spending summary.

# Development Environment

I wrote this program in Visual Studio Code on my Mac.

I used Python 3 to write the program and SQLite to store the expenses. I used Python's built-in `sqlite3` library to connect to the database and run SQL commands.

# Useful Websites

- [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [CSE 310 SQL Relational Databases Module](https://byui-cse.github.io/cse310-course/modules/sql_database/README.md)

# Future Work

- Add better error handling so the program does not crash if someone enters invalid information.
- Make the expense list and spending summary easier to read.
- Add a way to search for expenses by category or date.