from produto import Produto
from datetime import datetime as dt
from measure import Measure


class Alimento(Produto):
  

    def __init__(self, weight, type, name, price, expiration_date, brand, ID, amount=1, add_date=dt.today(), transgenic=False):
        
        super().__init__(name, price, expiration_date, brand, ID, amount, add_date)
        self.weight = weight
        self.type = type
        self.transgenic = transgenic
        self.CHANGE_SPEC = ['peso', 'tipo', 'transgenico']
        pass
    
    def __str__(self):
        return """
        -------------------------
        ID: %s
        Categoria: Alimento
        Produto: %s
        Preço: R$ %s 
        Peso: %s %s
        Tipo: %s
        Quantidade: %s Unidade(s)
        Data de adição: %s
        Data de Expiração: %s
        Transgenico: %s
        -------------------------
        """ % (self.ID, self.name, self.price, self.weight.value, self.weight.unit, self.type, self.amount, self.add_date, self.expiration_date, (lambda x: "Sim" if x else "Nao")(self.transgenic))
    
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type.title()

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = Measure(weight)

    @property
    def transgenic(self):
        return self._transgenic

    @transgenic.setter
    def transgenic(self, transgenic):
        self._transgenic = eval(transgenic)

    def updateData(self, key, value):
        keys_product = self.__dict__.copy()
        keys_product.pop('ID', None)
        keys_product.pop('CHANGE_TITLE', None)
        keys =  dict(zip(self.CHANGE_TITLE + self.CHANGE_SPEC, keys_product))

        self.__dict__[keys[key]] = value