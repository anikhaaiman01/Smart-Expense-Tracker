import csv


def save_expense(category, amount):

    with open(
        "expenses.csv",
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [category, amount]
        )


def load_expenses():

    expenses = []

    try:

        with open(
            "expenses.csv",
            "r"
        ) as file:

            reader = csv.reader(file)

            for row in reader:

                expenses.append(
                    {
                        "category": row[0],
                        "amount": float(row[1])
                    }
                )

    except FileNotFoundError:

        pass

    return expenses