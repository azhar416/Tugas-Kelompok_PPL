from Bank import *
from Loan import *
from Account import *
from Deposito import *

class Branch:
    __id: int
    __kota: str
    __list_account = []
    __list_loan = []
    __list_deposito = []

    def __init__(self, id, kota):
        self.__id = id
        self.__kota = kota

    def addAccount(self, account):
        self.__list_account.append(account)

    def removeAccount(self, account):
        self.__list_account.remove(account)

    def addLoan(self, loan):
        self.__list_loan.append(loan)

    def removeLoan(self, loan):
        self.__list_account.remove(loan)
    
    def addDeposito(self, deposito):
        self.__list_deposito.append(deposito)

    def removeDeposito(self, deposito):
        self.__list_deposito.remove(deposito)
    