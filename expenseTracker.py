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


