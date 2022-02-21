
import random
from re import M


class CellPhone:


    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    def set_manufact(self, manufact):
        self._manufact = manufact

    def set_model(self, model):
        self.model = model


    def set_model(self): 
        self.model = price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__price

