
import sqlite3

# Connect to the database
connection = sqlite3.connect("expenses.db")
cursor = connection.cursor()

# Create a table to store expenses
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    amount REAL,
    date TEXT
)
""")
connection.commit()

def add_expense():
    name = input("Expense name: ")
    category = input("Category: ")
    amount = float(input("Amount: "))
    expense_date = input("Date (YYYY-MM-DD): ")

    cursor.execute("""
    INSERT INTO expenses (name, category, amount, date)
    VALUES (?, ?, ?, ?)
    """, (name, category, amount, expense_date))

    connection.commit()
    print("Expense added!")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    for expense in expenses:
        print(expense)

def update_expense():
    view_expenses()
    expense_id = int(input("Enter the ID to update: "))

    name = input("New expense name: ")
    category = input("New category: ")
    amount = float(input("New amount: "))
    expense_date = input("New date (YYYY-MM-DD): ")

    cursor.execute("""
    UPDATE expenses
    SET name = ?, category = ?, amount = ?, date = ?
    WHERE id = ?
    """, (name, category, amount, expense_date, expense_id))

    connection.commit()
    print("Expense updated!")

def delete_expense():
    view_expenses()
    expense_id = int(input("Enter the ID to delete: "))

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?", (expense_id,)
    )

    connection.commit()
    print("Expense deleted!")

def show_summary():
    cursor.execute("""
    SELECT COUNT(*), SUM(amount), AVG(amount)
    FROM expenses
    """)
    summary = cursor.fetchone()

    print("\n===== SPENDING SUMMARY =====")
    print("-----------------------------")
    print("Number of expenses:", summary[0])
    print("Total spent: $", round(summary[1] or 0, 2))
    print("Average expense: $", round(summary[2] or 0, 2))
    print("=============================")

# Main menu
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Update expense")
    print("4. Delete expense")
    print("5. Spending summary")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        update_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        show_summary()
    elif choice == "6":
        connection.close()
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")