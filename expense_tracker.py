import json
from datetime import datetime

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expenses(expenses):
    try:
        amount = float(input("Enter amount:"))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("enter category: ").strip()
        description = input("Enter description: ").strip()
        date = input("Enter date (YYYY-MM-DD)or press Enter for today: ").strip()

        if not category:
            print("category cannot be empty.")
            return

        if not date:
            date = datetime.today().strftime("%y-%m-%d")
        else:
            datetime.strptime(date, "%y-%m-%d")

        expenses.append({
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        })

        save_expenses(expenses)
        print("Expenses added successfully!")

    except ValueError:
        print("Invalid amount or date. please try again.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}.{expense['date']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"Rs.{expense['amount']:.2f}"
        )

def filter_category(expenses):
    category = input("Enter category to search: ").strip().lower()

    results = [
        expense for expense in expenses
        if expense["category"].lower() == category
    ]

    view_expenses(results)

def filter_date(expenses):
    date = input("Enter date (YYYY-MM-DD):").strip()

    try:
        datetime.strptime(date, "%y-%m-%d")
        results = [e for e in expenses if e["date"] == date]
        view_expenses(results)
    except ValueError:
        print("Invalid date format.")

def monthly_total(expenses):
    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%y-%m")
        results =[
            e for e in expenses if
e["date"].startswith(month)
        ]

        total = sum(e["amount"] for e in results)
        print(f"Total expenses for {month}:Rs.{total:.2f}")

    except ValueError:
        print("Invalid month formate.")

def main():
    expenses = load_expenses()

    while True:
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Filter by Date")
        print("5. Monthly Total")
        print("6. Exit")

        choice = input("choose an option:").strip()
        print("you selected:", repr(choice))

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            print("showing expenses...")
            view_expenses(expenses)
        elif choice == "3":
            filter_category(expenses)
        elif choice == "4":
            filter_date(expenses)
        elif choice == "5":
            monthly_total(expenses)
        elif choice == "6":
            save_expenses(expenses)
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice. Select 1.6.")

if __name__ == "__main__":
    main()