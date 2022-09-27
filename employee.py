"""Employee pay calculator."""

from abc import ABC, abstractmethod

class Employee:
    def __init__(self, name, contract, commission = None):
        self.name = name
        self.contract = contract
        if commission:
            self.commission = commission
        else:
            self.commission = No_Commission()

    def get_pay(self):
        return self.contract.get_pay() + self.commission.get_pay()

    def __str__(self):
        return f'{self.name}{self.contract}{self.commission}.  Their total pay is {self.get_pay()}.'


class Contract(ABC):
    @abstractmethod
    def get_pay(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Salary_Contract(Contract):
    def __init__(self, contract_pay):
        self.contract_pay = contract_pay
    
    def get_pay(self):
        return self.contract_pay
    
    def __str__(self):
        return f' works on a monthly salary of {self.contract_pay}'

class Hourly_Contract(Contract):
    def __init__(self, contract_pay, number_of_hours):
        self.contract_pay = contract_pay
        self.number_of_hours = number_of_hours
    
    def get_pay(self):
        return self.contract_pay * self.number_of_hours
    
    def __str__(self):
        return f' works on a contract of {self.number_of_hours} hours at {self.contract_pay}/hour'


class Commission:
    @abstractmethod
    def get_pay(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Fixed_Commission(Commission):
    def __init__(self, commission_pay):
        self.commission_pay = commission_pay
    
    def get_pay(self):
        return self.commission_pay
    
    def __str__(self):
        return f' and receives a bonus commission of {self.commission_pay}'

class Per_Contract_Commission(Commission):
    def __init__(self, commission_pay, number_of_contracts):
        self.commission_pay = commission_pay
        self.number_of_contracts = number_of_contracts

    def get_pay(self):
        return self.commission_pay * self.number_of_contracts
    
    def __str__(self):
        return f' and receives a commission for {self.number_of_contracts}' \
            f' contract(s) at {self.commission_pay}/contract'

class No_Commission(Commission):
    def __init__(self):
        pass

    def get_pay(self):
        return 0
    
    def __str__(self):
        return ''


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee(name='Billie', contract=Salary_Contract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee(name='Charlie', contract=Hourly_Contract(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee(name='Renee', contract=Salary_Contract(3000), 
                commission=Per_Contract_Commission(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee(name='Jan', contract=Hourly_Contract(25, 150),
                commission=Per_Contract_Commission(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee(name='Robbie', contract=Salary_Contract(2000),
                commission=Fixed_Commission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee(name='Ariel', contract=Hourly_Contract(30, 120),
                commission=Fixed_Commission(600))