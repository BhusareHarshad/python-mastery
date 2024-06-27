import reader
import stock
import tableformat

portfolio = reader.read_csv_as_instances(
    r'C:\Users\HARSHAD BHUSARE\Desktop\SKILL UP\python-mastery\Data\portfolio.csv', stock.Stock)
formatter = tableformat.TextTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
# print(portfolio)
