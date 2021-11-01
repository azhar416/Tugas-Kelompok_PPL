from Deposito import *

class Pencairan:
    __saldo_cair: int
    __pinalti: int

    def __init__(self, saldo_cair, pinalti):
        self.__saldo_cair = saldo_cair
        self.__pinalti = pinalti

    def getSaldoCair(self):
        return self.__saldo_cair