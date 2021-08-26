class Account:
    def __init__(self, name, number, owner, balance=0):
        self.name = name
        self.balance = balance
        self.number = number
        self.owner = owner

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as f:
            name = f.readline()
        return cls(name)

    def set_balance(self, nbal):
        self.balance = nbal

    def get_balance(self):
        return self.balance

    def list_data(self):
        print()


class Employee:
    def __init__(self, name, role, number, salary):
        self.name = name
        self.role = role
        self.number = number
        self.salary = salary

    def get_name(self):
        return self.name

    def set_salary(self, nsal):
        self.salary = nsal

    def adjust_salary(self, amount):
        self.salary = self.salary + amount
        # check if not negative


class Customer:
    def __init__(self, name, number, accounts):
        self.name = name
        self.number = number
        self.accounts = accounts

    def get_name(self):
        return self.name


class Service:
    def __init__(self, type, number):
        self.type = type
        self.number = number

    def give_loan(self, account, amount, term):
        pass

    def give_creditcard(self, account, limit):
        pass



