from Branch import *

class Bank:
    __id: int
    __nama: str
    __list_branch = []

    def __init__(self, id, nama, alamat):
        self.__id = id
        self.__nama = nama

    def addBranch(self, branch):
        self.__list_branch.append(branch)

    def removeBranch(self, branch):
        self.__list_branch.remove(branch)