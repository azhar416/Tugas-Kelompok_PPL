from Branch import *
from Customer import *

class Deposito:
    __id: int
    __setoran: int
    __period: int
    __bunga: float
    __list_customer = []

    def __init__(self, id, setoran, period, bunga):
        self.__id = id
        self.__setoran = setoran
        self.__period = period
        self.__bunga = bunga

    def addCustomer(self, customer):
        self.__list_customer.append(customer)

    def removeCustomer(self, customer):
        self.__list_customer.remove(customer)

    def setPeriod(self, changePeriod):
        self.__period = changePeriod