expense = []
expense_cost = []


def add_expense(expense, expense_cost):
    while True:
        try:

            temp_expense = input("What was your expense?: ")
            if temp_expense.isdigit() == True:
                print("Please Enter A Valid Respone(Text)")
                continue
            expense.append(temp_expense)
            expense_cost.append(int(input("How Much was your expense?: ")))

            break

        except ValueError:
            print("Please Enter A Number for your price")


print("Welcome to Ensar's expense tracker")
running = True
while running == True:

    print(
        "1. Add An Expense\n"
        "2. View All Expenses\n"
        "3. Delete An Expense\n"
        "View Totals\n"
        "Quit\n"
    )

    try:
        user_choice = int(input("What would you like to do for today?: "))

    except ValueError:
        print("Please make sure to enter a number")

    if user_choice > 5 or user_choice < 0:
        print("Please Select One Of The Five Options")
        continue

    match user_choice:
        case 1:
            add_expense(expense, expense_cost)
    print(expense)
    print(expense_cost)
