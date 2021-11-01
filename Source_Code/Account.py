from datetime import date
from Customer import *
from Branch import *

class Account:
    __id: int
    __balance: int

    def __init__(self, id, balance):
        self.__id = id
        self.__balance = balance

    def getBalance(self):
        return self.__balance

class Saving_Account(Account):
    __min_balance: int
    __tanggal_dibuka = date.today()
    __list_customer = []

    def __init__(self, min_balance):
        self.__min_balance = min_balance

    def addCustomer(self, customer):
        self.__list_customer.append(customer)

    def removeCustomer(self, customer):
        self.__list_customer.remove(customer)

class Current_Account(Account):
    __interestRate: int
    __tanggal_dibuka = date.today()
    __list_customer = []

    def __init__(self, min_balance):
        self.__min_balance = min_balance

    def addCustomer(self, customer):
        self.__list_customer.append(customer)

    def removeCustomer(self, customer):
        self.__list_customer.remove(customer)