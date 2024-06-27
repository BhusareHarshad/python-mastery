import csv

def read_csv_as_dicts(filename, types):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    values = []
    for row in rows:
        dict = {name: func(val) for name, func, val in zip(headers, types, row)}
        values.append(dict)
    return values

def read_csv_as_instances(filename, cls):
    values = []
    
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            values.append(cls.from_row(row))
            
    return values
        