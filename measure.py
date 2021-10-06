class Measure:
    def __init__(self, w):
        self.w = w
        self.value = None
        self.unit = None
        pass
    
    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    @value.setter
    def value(self, w):
        self._value = self.w.split(' ')[0]

    @unit.setter
    def unit(self, w):
        self._unit = self.w.split(' ')[1].upper()