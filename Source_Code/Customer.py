from Account import *
from Deposito import *

class Customer:
    __id: int
    __nama: str
    __alamat: str
    __noTelp: str
    __savingAcc = Saving_Account()
    __currAcc = Current_Account()
    __deposito = Deposito()

    def __init__(self, id, nama, alamat, noTelp):
        self.__id = id
        self.__nama = nama
        self.__alamat = alamat
        self.__noTelp = noTelp

    def setSavingAcc(self, savingAcc):
        self.__savingAcc = savingAcc

    def setCurrAcc(self, currAcc):
        self.__currAcc = currAcc

    def setDeposito(self, deposito):
        self.__deposito = deposito