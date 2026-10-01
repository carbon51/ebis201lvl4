#Eli Baker
#Personal Expense Analyzer

#Set numbers list and initiate program
numbers = []
run_program = True
while run_program == True:

#Ask user to give number for expense

    expense = int(input("Enter a number for expense (or 0 to finish): "))
    while expense < 0:
        print("Expense cannot be negative.")
        expense = int(input("Enter a number for expense (or 0 to finish): "))
    numbers.append(int(expense))

#Once user enters '0', print results

    if expense == 0:
        print("Expense summary:")
        print(f"Number of expenses: {len(numbers)}")
        print(f"Total: ${sum(numbers)}")
        print(f"Average: ${round(sum(x for x in numbers if x != 0) / len([x for x in numbers if x != 0]), 2)}")
        print(f"Smallest expense: ${min(x for x in numbers if x != 0)}")
        print(f"Largest expense ${max(numbers)}")

#Sort results and ask if they want to calculate again

        print(f"Small expenses: ${[x for x in numbers if 0 < x <= 25]}")
        print(f"Moderate expenses: ${[x for x in numbers if 25 < x <= 100]}")
        print(f"Large expesnes: ${[x for x in numbers if x > 100]}")
        input = input("Would you like to calculate again? (y/n) ")
        if input == "y":
            run_program = True
            numbers = []
        elif input == "n":
            print ("Calculations complete.")
            run_program = False