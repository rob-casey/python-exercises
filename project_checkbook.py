import csv
import datetime


def add_transaction(amount, description):
    date = datetime.datetime.now().strftime("%m-%d-%Y")
    time = datetime.datetime.now().strftime("%H:%M:%S")
    with open("checkbook.csv", "a", newline="") as file:
        fieldnames = ["date", "time", "amount", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"date": date, "time": time, "amount": amount, "description": description})


def read_balance():
    balance = 0
    with open("checkbook.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            balance += float(row["amount"])
    return balance


def save_balance(balance):
    with open("balance.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([balance])


def main():
    balance = 0
    try:
        with open("balance.csv", "r") as file:
            reader = csv.reader(file)
            balance = float(next(reader)[0])
    except FileNotFoundError:
        balance = 0
    except StopIteration:
        balance = 0

    print(" ~~~ Welcome to your terminal checkbook! ~~~")
    print(" ")

    while True:

        print("What would you like to do? ")
        print(" ")
        print("1. View balance")
        print("2. Record a debit (withdrawal)")
        print("3. Record a credit (deposit)")
        print("4. Exit")
        print(" ")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(" ")
            print("Your balance is:", balance)
            print(" ")
        elif choice == 2:
            print(" ")
            amount = float(input("Enter the amount to debit: "))
            balance -= amount
            add_transaction(-amount, "Debit")
            save_balance(balance)
            print("Your remaining balance is:", balance)
            print(" ")
        elif choice == 3:
            print(" ")
            amount = float(input("Enter the amount to add: "))
            balance += amount
            add_transaction(amount, "Credit")
            save_balance(balance)
            print(" ")
        elif choice == 4:
            break

        else:
            print(" ")
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()