
bank = {
    "account": None,
    "balance": 0,
    "locker": []
}


def create_account():
    if bank["account"] is not None:
        print("Account already exists!")
        return

    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    age = int(input("Enter your age: "))
    phone = input("Enter your mobile number: ")

    if age <= 0 or len(phone) != 10 or not phone.isdigit():
        print("Invalid age or mobile number!")
        return

    account_number = 1001

    bank["account"] = {
        "name": name,
        "age": age,
        "phone": phone,
        "account_number": account_number
    }

    print("\nAccount created successfully!")
    print("Account Holder:", name)
    print("Account Number:", account_number)
    print("Opening Balance: ₹", bank["balance"])


def loan_section():
    if bank["account"] is None:
        print("Please create an account first!")
        return

    age = bank["account"]["age"]
    income = int(input("Enter your monthly income: ₹"))

    # Demo eligibility rules for this project
    if age < 18 or income < 15000:
        print("Sorry, you are not eligible under demo rules.")
        return

    print("\n--- LOAN TYPES ---")
    print("1. Education Loan")
    print("2. Home Loan")
    print("3. Car Loan")
    print("4. Personal Loan")
    print("5. Business Loan")

    choice = input("Choose loan type: ")

    loans = {
        "1": "Education Loan",
        "2": "Home Loan",
        "3": "Car Loan",
        "4": "Personal Loan",
        "5": "Business Loan"
    }

    if choice not in loans:
        print("Invalid loan choice!")
        return

    amount = int(input("Enter required loan amount: ₹"))

    if amount <= 0:
        print("Enter a valid loan amount!")
        return

    print("\nLoan application submitted successfully!")
    print("Loan Type:", loans[choice])
    print("Requested Amount: ₹", amount)
    print("Status: Pending verification")


def credit_account():
    if bank["account"] is None:
        print("Please create an account first!")
        return

    amount = int(input("Enter deposit amount: ₹"))

    if amount <= 0:
        print("Amount must be greater than zero!")
        return

    bank["balance"] += amount

    print("Money deposited successfully!")
    print("Current Balance: ₹", bank["balance"])


def debit_account():
    if bank["account"] is None:
        print("Please create an account first!")
        return

    amount = int(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Amount must be greater than zero!")

    elif amount > bank["balance"]:
        print("Insufficient balance!")

    else:
        bank["balance"] -= amount
        print("Withdrawal successful!")
        print("Remaining Balance: ₹", bank["balance"])


def check_balance():
    if bank["account"] is None:
        print("Please create an account first!")
        return

    print("Available Balance: ₹", bank["balance"])


def account_details():
    if bank["account"] is None:
        print("Please create an account first!")
        return

    print("\n--- ACCOUNT DETAILS ---")
    print("Name:", bank["account"]["name"])
    print("Age:", bank["account"]["age"])
    print("Mobile:", bank["account"]["phone"])
    print("Account Number:", bank["account"]["account_number"])
    print("Balance: ₹", bank["balance"])


def locker_section():
    if bank["account"] is None:
        print("Please create an account first!")
        return

    print("\n--- BANK LOCKER ---")
    print("1. Store Gold/Silver")
    print("2. Store Cash")
    print("3. View Locker")
    print("4. Back to Main Menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        metal = input("Enter gold or silver: ").strip().lower()
        grams = float(input("Enter weight in grams: "))

        if metal not in ["gold", "silver"] or grams <= 0:
            print("Invalid metal or weight!")
            return

        bank["locker"].append({
            "type": metal,
            "quantity": grams,
            "unit": "grams"
        })

        print(metal.title(), "stored in locker successfully!")

    elif choice == "2":
        amount = int(input("Enter cash amount to store: ₹"))

        if amount <= 0:
            print("Enter a valid amount!")
            return

        bank["locker"].append({
            "type": "Cash",
            "quantity": amount,
            "unit": "rupees"
        })

        print("Cash entry added to locker!")

    elif choice == "3":
        if not bank["locker"]:
            print("Locker is empty!")
        else:
            print("\n--- LOCKER CONTENTS ---")
            for item in bank["locker"]:
                print(
                    item["type"].title(),
                    ":",
                    item["quantity"],
                    item["unit"]
                )

    elif choice == "4":
        return

    else:
        print("Invalid locker choice!")


print("Welcome to Banking Management System!")

while True:
    print("\n========== MAIN MENU ==========")
    print("1. Create Account")
    print("2. Loan Section")
    print("3. Credit Account (Deposit)")
    print("4. Debit Account (Withdraw)")
    print("5. Locker Section")
    print("6. Check Balance")
    print("7. Account Details")
    print("8. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            create_account()

        elif choice == "2":
            loan_section()

        elif choice == "3":
            credit_account()

        elif choice == "4":
            debit_account()

        elif choice == "5":
            locker_section()

        elif choice == "6":
            check_balance()

        elif choice == "7":
            account_details()

        elif choice == "8":
            print("Thank you for using our banking system!")
            break

        else:
            print("Invalid choice! Please select 1 to 8.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
