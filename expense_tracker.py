from expense import Expense
import datetime
import calendar


def main():
    print(f"Running expense tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000

    # Get user input for expense
    expense = get_user_expense()

    # Write their expense to a file 
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarise expenses
    summarise_expense(expense_file_path, budget)

def get_user_expense():
    print(f"Getting user Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_categories = [
        "🍔 Food", 
        "🏠 Home", 
        "🏢 Work", 
        "🎉 Fun", 
        "➕ Misc",
    ] 

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")  # This prints the full category list
        
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            ) 
            return new_expense
        else:
            print("Invalid category. Please try again!")

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving user Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")

def summarise_expense(expense_file_path, budget):
    print(f"Summarising User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category
            )
            expenses.append(line_expense)

     
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount


    print("Expenses by Category")
    for key, amount in amount_by_category.items():
        print(f"  {key}: €{amount:.2f}")


    total_spent = sum([x.amount for x in expenses])
    print(f"Total Spent: €{total_spent}")

    remaining_budget = budget - total_spent
    print(f"Remaining Budget: €{remaining_budget}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month -  now.day

    daily_budget = remaining_budget / remaining_days
    print(f"Budget per day: €{daily_budget:.2f}")



if __name__ == "__main__":
    main()