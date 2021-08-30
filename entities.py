class Account:
    def __init__(self, name, number, owner, balance=0):
        self.name = name
        self.number = number
        self.owner = owner
        self.balance = balance


    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as f:
            name = f.readline()
        return cls(name)

    def set_balance(self, nbal):
        self.balance = nbal

    def get_balance(self):
        return self.balance

    def get_number(self):
        return self.number

    def get_name(self):
        return self.name

    def get_owner(self):
        return self.owner

    def list_data(self):
        return ('Account: {} Name: {} - Balance: {} - Owner: {}'.format(
            self.number, self.name, self.balance, self.owner))


class Employee:
    def __init__(self, name, role, number, salary):
        self.name = name
        self.role = role
        self.number = number
        self.salary = salary

    def set_salary(self, nsal):
        self.salary = nsal

    def adjust_salary(self, amount):
        self.salary = self.salary + amount
        # check if not negative

    @property
    def get_name(self):
        return self.name

    def get_role(self):
        return self.role

    def get_number(self):
        return self.number

    def get_salary(self):
        return self.salary

    def list_data(self):
        return('Employee Name: {} Number: {} - Salary: {} - Role: {}'.format(
            self.name, self.number, self.salary, self.role))


class Customer:
    def __init__(self, name, number, accounts):
        self.name = name
        self.number = number
        self.accounts = accounts

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_accounts(self):
        return self.accounts

    def list_data(self):
        return('Customer Name: {} Number: {} - Accounts: {}'.format(
            self.name, self.number, self.accounts))


class Service:
    def __init__(self, accnumber):
        self.accnumber = accnumber


class Loan(Service):
    def __init__(self, owning_acc, amount, term):
        self.owning_acc = owning_acc
        self.amount = amount
        self.term = term

    def list_data(self):
        return('Loan owning Account: {} Amount: {} - Term: {}'.format(
            self.owning_acc, self.amount, self.term))

class CreditCard(Service):
    def __init__(self, owning_acc, amount):
        self.owning_acc = owning_acc
        self.amount = amount

    def list_data(self):
        return('Card owning Account: {} Limit: {}'.format(
            self.owning_acc, self.amount))