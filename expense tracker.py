import os
import json

# File to store expenses
EXPENSES_FILE = "expenses.json"

# Function to load expenses from file
def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save expenses to file
def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file)

# Function to add an expense
def add_expense(expenses):
    category = input("Enter the expense category (e.g., Food, Transport, etc.): ")
    amount = float(input("Enter the amount spent: "))
    expense = {"category": category, "amount": amount}
    expenses.append(expense)
    print(f"Expense of {amount} added under '{category}' category.")
    save_expenses(expenses)

# Function to display all expenses
def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nExpenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. Category: {expense['category']}, Amount: {expense['amount']}")

# Function to calculate the total expenses
def calculate_total(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: {total}")

# Function to display the menu
def display_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Exit")

# Main program logic
def main():
    expenses = load_expenses()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            display_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
