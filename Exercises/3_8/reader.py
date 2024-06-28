from abc import ABC, abstractmethod
import csv

class CSVParser(ABC):
    def parser(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
                
    @abstractmethod
    def make_record(self, headers, row):
        pass
    
class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_rows(row)        
    