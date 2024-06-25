class Stock:
    _types = [str, int, float]
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    @classmethod
    def from_row(cls, row):
        values = [func(v) for func, v in zip(cls._types, row)]
        return cls(*values)
    
    @property
    def shares(self):
        self._shares
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected an Integer")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value
    
    @property
    def cost(self):
        return self.shares * self.price