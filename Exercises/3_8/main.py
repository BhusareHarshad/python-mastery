import stock
from reader import InstanceCSVParser

f = InstanceCSVParser(stock.Stock)

row = ('GOG', 100, 32.2)
f.make_record(row)