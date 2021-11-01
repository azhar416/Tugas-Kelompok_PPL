from Customer import *
from Branch import *

class Loan:
    __id: int
    __jumlah: int
    __type: str
    __list_customer = []

    def __init__(self, id, jumlahPinjaman, type):
        self.__id = id
        self.__jumlah = jumlahPinjaman
        self.__type = type

    def addCustomer(self, customer):
        self.__list_customer.append(customer)

    def removeCustomer(self, customer):
        self.__list_customer.remove(customer)

    def getJumlahPinjaman(self):
        return self.__jumlah