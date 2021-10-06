from datetime import datetime as dt
from abc import ABC, abstractmethod

class Produto(ABC):

    def __init__(self, name, price, expiration_date, brand, ID, amount=1, add_date=dt.today()):

        self.name = name
        self.price = price
        self.expiration_date = expiration_date
        self.brand = brand
        self.amount = amount
        self.add_date = add_date 
        self.ID = ID
        self.CHANGE_TITLE = ['nome', 'preco', 'data de validade', 'marca', 'quantidade', 'data de adicao']
        pass
    
    def isNearExpiration(self):
        return (self.expiration_date - self.add_date).days <= 30
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = abs(float(price))
    
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = abs(int(amount))

    @property
    def add_date(self):
        return self._add_date

    @add_date.setter
    def add_date(self, date):
        if isinstance(date, str):
            self._add_date = dt.strptime(date, '%d/%m/%y')
        else: self._add_date = date
      
    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, date):
        self._expiration_date = dt.strptime(date, '%d/%m/%y')

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @abstractmethod
    def updateData(self, key, value):
        return None