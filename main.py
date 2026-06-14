from ExpenseManager import (
    add_expense,
    view_expenses,
    category_summary
)

from FileHandler import load_expenses


expenses = load_expenses()


while True:

    print("\n===== SMART EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_expense(expenses)

    elif choice == "2":

        view_expenses(expenses)

    elif choice == "3":

        category_summary(expenses)

    elif choice == "4":

        print("Thank you for using Expense Tracker!")
        break

    else:

        print("Invalid choice")