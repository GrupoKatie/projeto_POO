from produto import Produto
from datetime import datetime as dt
from measure import Measure

class Bebida(Produto):

    def __init__(self, volume, type, name, price, expiration_date, brand, ID, amount=1, add_date=dt.today(), alcohol=False):
        
        super().__init__(name, price, expiration_date, brand, ID, amount, add_date)
        self.volume = volume
        self.type = type
        self.alcohol = alcohol
        self.CHANGE_SPEC = ['volume', 'tipo', 'alcoolico']
        pass
    
    def __str__(self):
        return """
        -------------------------
        ID: %s
        Categoria: Bebida
        Produto: %s
        Preço: R$ %s 
        Volume: %s %s
        Tipo: %s
        Quantidade: %s Unidade(s)
        Data de adição: %s
        Data de Expiração: %s
        Alcólica: %s
        -------------------------
        """ % (self.ID, self.name, self.price, self.volume.value, self.volume.unit, self.type, self.amount, self.add_date, self.expiration_date, (lambda x: "Sim" if x else "Nao")(self.alcohol))
    
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type.title()

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._volume = Measure(volume)
    
    @property
    def alcohol(self):
        return self._alcohol

    @alcohol.setter
    def alcohol(self, alcohol):
        self._alcohol = eval(alcohol)

    def updateData(self, key, value):
        keys_product = self.__dict__.copy()
        keys_product.pop('ID', None)
        keys_product.pop('CHANGE_TITLE', None)
        keys =  dict(zip(self.CHANGE_TITLE + self.CHANGE_SPEC, keys_product))

        self.__dict__[keys[key]] = value