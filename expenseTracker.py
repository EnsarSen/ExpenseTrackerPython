expenses = []


def add_expense(expense):
    while True:
        try:

            temp_expense = input("What was your expense?: ")
            if temp_expense.isdigit() == True:
                print("Please Enter A Valid Respone(Text)")
                continue

            expense_cost = float(input("How Much was your expense?: "))
            if expense_cost < 0:
                print("*******************************")
                print("Please Enter A Positive Number")
                print("*******************************")
                continue
            expenses.append({"description": temp_expense, "cost": expense_cost})

            break

        except ValueError:
            print("Please Enter A Number for your price")


def show_expense(expenses):
    expense_total = 0
    print("--- All Expenses ---")

    count = 1
    for expense in expenses:

        print(f"{count}. {expense['description']:<15}${expense['cost']:.2f}")
        expense_total += expense["cost"]
        count += 1
    print("\n")
    print("--------------------")
    print(f"Total {expense_total:<15}")


def delete_expense(expenses):
    expense_list = len(expenses)
    while True:

        if not expenses:
            print("*****************")
            print("No Expenses Found")
            print("*****************")
            break

        try:
            selected_expense = int(
                input("Which expense would you like to remove?(select by number): ")
            )

        except ValueError:
            print("Please Enter A Number")

            continue
        if expense_list < selected_expense:
            print("**********************************")
            print("Please select an available expense")
            print("**********************************")
            break

        expenses.pop(selected_expense - 1)
        break


print("Welcome to Ensar's expense tracker")
running = True
while running == True:

    print(
        "1. Add An Expense\n"
        "2. View All Expenses\n"
        "3. Delete An Expense\n"
        "4. Quit\n"
    )

    try:
        user_choice = int(input("What would you like to do for today?: "))

    except ValueError:
        print("***********************************")
        print("Please make sure to enter a WHOLE number(ex. 1, 2, 3, 4, 5)")
        print("***********************************")
        continue

    if user_choice > 5 or user_choice <= 0:
        print("*************************************")
        print("Please Select One Of The Five Options")
        print("*************************************")
        continue

    match user_choice:
        case 1:
            add_expense(expenses)
        case 2:
            show_expense(expenses)
        case 3:
            delete_expense(expenses)
        case 4:
            break
