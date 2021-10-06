from produto import Produto
from datetime import datetime as dt

class Papelaria(Produto):

    def __init__(self, color, type, name, price, expiration_date, brand, ID, amount=1, add_date=dt.today(), recyclable=False):
        
        super().__init__(name, price, expiration_date, brand, ID, amount, add_date)
        self.type = type
        self.color = color
        self.recyclable = recyclable
        self.CHANGE_SPEC = ['cor', 'tipo', 'reciclavel']
        pass
    
    def __str__(self):
        return """
        -------------------------
        ID: %s
        Categoria: Papelaria
        Produto: %s
        Preço: R$ %s 
        Cor: %s
        Tipo: %s
        Quantidade: %s Unidade(s)
        Data de adição: %s
        Data de Expiração: %s
        Reciclavel: %s
        -------------------------
        """ % (self.ID, self.name, self.price, self.color, self.type, self.amount, self.add_date, self.expiration_date, (lambda x: "Sim" if x else "Nao")(self.recyclable))
    
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type.title()

    @property
    def recyclable(self):
        return self._recyclable

    @recyclable.setter
    def recyclable(self, recyclable):
        self._recyclable = eval(recyclable)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
    
    def updateData(self, key, value):
        keys_product = self.__dict__.copy()
        keys_product.pop('ID', None)
        keys_product.pop('CHANGE_TITLE', None)
        keys =  dict(zip(self.CHANGE_TITLE + self.CHANGE_SPEC, keys_product))

        self.__dict__[keys[key]] = value