

# create a list of sample expenses with dictionaries
expenses = [
    {"category": "food",          "amount": 15.50, "date": "2025-02-16"},
    {"category": "transport",     "amount": 5.00,  "date": "2025-02-16"},
    {"category": "entertainment", "amount": 20.00, "date": "2025-02-17"}
]



#create a set of categories
category_set = {expense['category'] for expense in expenses}
#print(category_set)

#verify whether the input amount is numeric
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

from datetime import datetime

#verify whether the date is valid
def is_valid_date(date_str, date_format="%Y-%m-%d"):
    try:
        parsed_date = datetime.strptime(date_str, date_format)
    except ValueError:
        return False
    
    # Compare the parsed date with the current date and time.
    if parsed_date > datetime.now():
        return False
    
    return True


def adding_expense():
    #Collect the data of new expense from user
    print("Please input the following data of your new expense:")
    category = input("Category:").lower()
    amount = input("Amount:")
    date = input("Date:")
    
    #Verify the inputs
    
    #verify if the category exists
    if category not in category_set:
        print(category, " does not exist.")
        userinput = input("Do you want to create this new category? ((Y)es/(N)o)" )
        if userinput.upper() == 'N':
            print("The new expense is not added. Please input again later!")
            return
    
    #verify if the amount is numeric
    if not is_numeric(amount):
        print("The amount is not a number. Please input again later!")
        return
    
    #verify if the date is valid
    if not is_valid_date(date):
        print("The date is not a valid date. Please input again later!")
        return  
    
    #create the new expense dictionary
    expense = { "category": category, "amount": amount, "date": date }
    
    #Add the new expense to the list of expenses
    expenses.append(expense)
       
    
    
# Main program
def main():
    adding_expense()
    for expense in expenses:
        print(f"On {expense['date']}, you spent ${expense['amount']} on {expense['category']}.")

if __name__ == "__main__":
    main()