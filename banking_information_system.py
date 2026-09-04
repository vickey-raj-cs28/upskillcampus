"""
Banking Information System
Python Internship Project - upSkill Campus

A beginner-friendly console banking application demonstrating:
- input()
- lists/dictionaries
- append()
- functions using def
- file handling
- basic validation
"""

import json
import os

DATA_FILE = "accounts.json"


def load_accounts():
    """Load account records from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_accounts(accounts):
    """Save account records to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(accounts, file, indent=4)


def find_account(accounts, account_number):
    """Return an account matching the account number."""
    for account in accounts:
        if account["account_number"] == account_number:
            return account
    return None


def create_account(accounts):
    print("\n--- Create Account ---")
    name = input("Enter customer name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    account_number = input("Enter account number: ").strip()

    if not account_number:
        print("Account number cannot be empty.")
        return

    if find_account(accounts, account_number):
        print("An account with this number already exists.")
        return

    try:
        opening_balance = float(input("Enter opening balance: "))
        if opening_balance < 0:
            print("Opening balance cannot be negative.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    account = {
        "account_number": account_number,
        "name": name,
        "balance": opening_balance,
        "transactions": [f"Account created with balance Rs. {opening_balance:.2f}"]
    }

    accounts.append(account)
    save_accounts(accounts)
    print("Account created successfully.")


def deposit_money(accounts):
    print("\n--- Deposit Money ---")
    account_number = input("Enter account number: ").strip()
    account = find_account(accounts, account_number)

    if not account:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Deposit must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    account["balance"] += amount
    account["transactions"].append(f"Deposited Rs. {amount:.2f}")
    save_accounts(accounts)
    print(f"Deposit successful. New balance: Rs. {account['balance']:.2f}")


def withdraw_money(accounts):
    print("\n--- Withdraw Money ---")
    account_number = input("Enter account number: ").strip()
    account = find_account(accounts, account_number)

    if not account:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Withdrawal must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount > account["balance"]:
        print("Insufficient balance.")
        return

    account["balance"] -= amount
    account["transactions"].append(f"Withdrawn Rs. {amount:.2f}")
    save_accounts(accounts)
    print(f"Withdrawal successful. New balance: Rs. {account['balance']:.2f}")


def check_balance(accounts):
    print("\n--- Check Balance ---")
    account_number = input("Enter account number: ").strip()
    account = find_account(accounts, account_number)

    if not account:
        print("Account not found.")
        return

    print(f"Customer: {account['name']}")
    print(f"Account Number: {account['account_number']}")
    print(f"Current Balance: Rs. {account['balance']:.2f}")


def show_transactions(accounts):
    print("\n--- Transaction History ---")
    account_number = input("Enter account number: ").strip()
    account = find_account(accounts, account_number)

    if not account:
        print("Account not found.")
        return

    print(f"\nTransactions for {account['name']}:")
    for index, transaction in enumerate(account["transactions"], start=1):
        print(f"{index}. {transaction}")


def main():
    accounts = load_accounts()

    while True:
        print("\n========== BANKING INFORMATION SYSTEM ==========")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_money(accounts)
        elif choice == "3":
            withdraw_money(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            show_transactions(accounts)
        elif choice == "6":
            print("Thank you for using the Banking Information System.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
