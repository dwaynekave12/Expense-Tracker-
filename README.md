# Expense Tracker

## Overview
This is a simple Expense Tracker application built using Python. It allows users to:
- Input their expenses with a name, category, and amount.
- Save expenses to a CSV file.
- Summarize expenses by category and compare them against a budget.
- Calculate a daily spending budget based on remaining days in the month.

## Features
- **Expense Entry**: Users can enter expense details (name, amount, category).
- **CSV Storage**: Expenses are saved to a CSV file for persistence.
- **Expense Summary**: The application calculates total expenses and categorizes them.
- **Budget Calculation**: Determines remaining budget and daily spending limit.

## Prerequisites
- Python 3.x installed

## Installation
1. Clone the repository or copy the script.
2. Ensure Python 3 is installed on your system.
3. Install dependencies (if needed, though none are required for this script).

## Usage
Run the script by executing:
```sh
python expense_tracker.py
```

## How It Works
1. The user is prompted to enter an expense (name, amount, category).
2. The expense is saved to `expenses.csv`.
3. The program reads expenses from the CSV file and categorizes them.
4. It calculates the total spent, remaining budget, and recommended daily spending.

## Example Expense Categories
- 🍔 Food
- 🏠 Home
- 🏢 Work
- 🎉 Fun
- ➕ Misc

## Future Enhancements
- Convert into a web-based application with a frontend.
- Store expenses in a database instead of a CSV file.
- Implement authentication and user-specific expense tracking.

## Author
- Developed by Dwayne Kave

