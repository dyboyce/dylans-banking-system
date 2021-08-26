import entities
# read in from file
# create the lists of accounts, custs, etc

print("Welcome to the Banking System! Please type 'help' to see commands. "
      "\n 'x' 'q' and 'exit' will all exit the program")

while True:
    user_in = input()
    if user_in == 'x' or user_in == 'q' or user_in == 'quit':
        break
    if user_in == 'help':
        print("Available Commands-")
        print("create: Will allow you to create an Employee, "
              "Account, Customer, or Service.")
        print("list: Will print out list of specified type.")
        print("print: Will print all data on specified Employee,"
              " Account, or Customer.")
        print("loan: Gives a loan to a customer.")
        print("credit: Opens a line of credit for a customer.")
        print("give raise: Increases an employees salary.")
        print("set salary: Sets an arbitrary Salary.")
        print("change role: Changes an Employee's job.")
        print("withdraw: Removes money from an account.")
        print("deposit: Puts money into an account.")
        print("show balance: Displays the account balance.")

    if user_in == 'create':
        print('What would you like to create?')
        print('Please enter one of the following format '
              'options starting with the type first :')
        print('Employee, name, role, number, salary')
        print('Customer, name, number, account, account,...')
        print('Account, name, number, owner, balance')
        print('Service, type, account, amount')
        create_in = input()
        create_strs = create_in.split(',')

    if user_in == 'list':
        print("What type would you like to view: Accounts,"
              " Employees, Customers, or Services")
        list_in = input()
        if list_in == 'Accounts':
            pass
        elif list_in == 'Employees':
            pass
        elif list_in == 'Customers':
            pass
        elif list_in == 'Services':
            pass
        else:
            print("Please select one of the four choices")

# read out to file