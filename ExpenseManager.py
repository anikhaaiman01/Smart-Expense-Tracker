from FileHandler import save_expense


def add_expense(expenses):

    category = input("Enter category: ")

    try:

        amount = float(
            input("Enter amount ₹: ")
        )

    except ValueError:

        print("Invalid amount")
        return

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    save_expense(category, amount)

    print("Expense Added Successfully")


def view_expenses(expenses):

    if len(expenses) == 0:

        print("No expenses found")
        return

    total = 0

    print("\nExpense History")

    for expense in expenses:

        print(
            f"{expense['category']} - ₹{expense['amount']}"
        )

        total += expense["amount"]

    print(f"\nTotal Spending: ₹{total}")


def category_summary(expenses):

    summary = {}

    for expense in expenses:

        category = expense["category"]

        amount = expense["amount"]

        if category in summary:

            summary[category] += amount

        else:

            summary[category] = amount

    print("\nCategory Summary")

    for category, amount in summary.items():

        print(
            f"{category}: ₹{amount}"
        )