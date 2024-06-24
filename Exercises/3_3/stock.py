class Stock:
    types = (str, int, float)
    def __init__(self, names, shares, price):
        pass
    
    @classmethod
    def from_row(cls, row):
        values = [func(v) for func, v in zip(cls.types, row)]
        return cls(*values)


# class Stock:
#     types = (str, int, float)
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price

#     @classmethod
#     def from_row(cls, row):
#         values = [func(val) for func, val in zip(cls.types, row)]
#         return cls(*values)


# class Stock:
#     types = (str, int, float)
    
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price

#     @classmethod
#     def from_row(cls, row):
#         if len(row) != len(cls.types):
#             raise ValueError("Row has incorrect number of elements")
#         try:
#             values = [func(val) for func, val in zip(cls.types, row)]
#         except ValueError as e:
#             raise ValueError(f"Error converting row: {e}")
#         return cls(*values)