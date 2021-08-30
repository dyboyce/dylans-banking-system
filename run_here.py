from entities import Customer, Account, Employee, Service, Loan, CreditCard
import logging
import os
import time

timstr = time.strftime("%Y%m%d-%H%M%S") + 'standard.log'
log_dir = os.path.join(os.path.normpath(os.getcwd() + os.sep), 'logs')
log_fname = os.path.join(log_dir, timstr)

logging.basicConfig(filename=log_fname, filemode='w',
                    format='%(asctime)s - %(message)s', level=logging.DEBUG)

Accounts = []
Customers = []
Employees = []
Services = []

Customers.append(Customer('Norbert Nunez', 1463234285, 595686))
Customers.append(Customer('Mark Mattise', 1104943434, 8679546845))
Customers.append(Customer('Pablo Pica', 77735535345, 44340235))
Customers.append(Customer('Yanni Chalani', 99999932, 65858855555))

Accounts.append(Account('Checking', 959578359, 'Joni Mitcheeel', 40000))
Accounts.append(Account('Savings', 8739020111, 'David Webb', 9001))
Accounts.append(Account('Jonah Checking',
                        111111334124, 'Jonah Jameson', 152425555))
Accounts.append(Account('Mandy Savings', 6306548094, 'Mandy Morse', 3.50))

Employees.append(Employee('Dick Van Dyke', 'Chimney Sweep', 6582228, 5))
Employees.append(Employee('Mary Poppins', 'Nanny', 4010111, 2000000))
Employees.append(Employee('Willy Wonka', 'CEO', 1, 500000000))
Employees.append(Employee('Oompah Loompah', 'Candy Production', 66523322, 500))

print("Welcome to the Banking System! Please type 'help' to see commands. "
      "\n 'x' 'q' and 'exit' will all exit the program")

while True:
    try:
        user_in = input()
        if user_in == 'x' or user_in == 'q' or user_in == 'quit':
            logging.info("Exit command called.")
            break
        elif user_in == 'help':
            print("Available Commands-")
            print("create: Will allow you to create an Employee, "
                  "Account, Customer, or Service.")
            print("list: Will print out list of specified type.")

        elif user_in == 'create':
            print('What would you like to create?')
            print('Please enter one of the following format '
                  'options starting with the type first :')
            print('Employee, name, role, number, salary')
            print('Customer, name, number, account, account,...')
            print('Account, name, number, owner, balance')
            print('Service, type, account, amount')
            create_in = input()
            cr_strs = create_in.split(',')
            if cr_strs[0] == "Employee":
                try:
                    Employees.append(Employee(
                        cr_strs[1], cr_strs[2], cr_strs[3], cr_strs[4]))
                except(AttributeError, IndexError):
                    logging.warning(logging.exception(
                        'Employee Creation Error'))
                    print("Please format your request correctly")
                else:
                    print("Employee added to index.")
            elif cr_strs[0] == "Account":
                try:
                    logging.debug('Attempting '
                                  'to make an account: %s, %s, %s, %s',
                                  cr_strs[1], cr_strs[2],
                                  cr_strs[3], cr_strs[4])
                    Accounts.append(Account(
                        cr_strs[1], cr_strs[2], cr_strs[3], cr_strs[4]))

                except(AttributeError, IndexError):
                    logging.warning(logging.exception(
                        'Account Creation Error'))
                    print("Please format your request correctly")
                else:
                    print("Account added to index.")
            elif cr_strs[0] == "Customer":
                try:
                    logging.debug('Attempting to make a customer:'
                                  ' %s, %s, %s',
                                  cr_strs[1], cr_strs[2],
                                  cr_strs[3])
                    Customers.append(Customer(
                        cr_strs[1], cr_strs[2], cr_strs[3]))
                except(AttributeError, IndexError):
                    logging.warning(logging.exception(
                        'Customer Creation Error'))
                    print("Please format your request correctly")
                else:
                    print("Customer added to index.")
            elif cr_strs[0] == "Service":
                if str(cr_strs[1]) == str(' Loan'):
                    try:
                        logging.debug('Attempting to make a Loan:'
                                      ' %s, %s, %s',
                                      cr_strs[2], cr_strs[3],
                                      cr_strs[4])
                        Services.append(Loan(
                            cr_strs[2], cr_strs[3], cr_strs[4]))
                    except(AttributeError, IndexError):
                        logging.warning(logging.exception(
                            'Loan Creation Error'))
                        print("Please format your request correctly")
                    else:
                        print("Loan added to index")
                else:
                    try:
                        logging.debug('Attempting to make a Creditcard:'
                                      ' %s, %s',
                                      cr_strs[1], cr_strs[2])
                        Services.append(CreditCard(
                            cr_strs[1], cr_strs[2]))
                    except(AttributeError, IndexError):
                        logging.warning(logging.exception(
                            'CreditCard Creation Error'))
                        print("Please format your request correctly.")
                    else:
                        print("Credit Card Added to index")

        elif user_in == 'list':
            logging.debug('List command entered.')
            print("What type would you like to view: Accounts,"
                  " Employees, Customers, or Services")
            list_in = input()
            if list_in == 'Accounts':
                for i in Accounts:
                    print(i.list_data())
            elif list_in == 'Employees':
                for i in Employees:
                    print(i.list_data())
            elif list_in == 'Customers':
                for i in Customers:
                    print(i.list_data())
            elif list_in == 'Services':
                for i in Services:
                    print(i.list_data())
            else:
                logging.debug("List ended with no valid input")
                print("Please select one of the four choices")
        else:
            logging.debug('Reached end of '
                          'input without valid response.')
            print('Please select a properly formatted choice')
    except ValueError:
        print('Please select an approved Value')

