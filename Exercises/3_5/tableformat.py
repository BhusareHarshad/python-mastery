
# def print_table(records, fields):
#     print(' '.join('%10s' % fieldname for fieldname in fields))
#     print(('-'*10 + ' ')*len(fields))
#     for record in records:
#         print(' '.join('%10s' % getattr(record, fieldname) for fieldname in fields))

def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
        
class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()
    
    def row(self, rowdata):
        raise NotImplementedError()
    
    
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))
        
    def row(self, rowdata):
        print(' '.join('%10s' % r for r in rowdata))
    
    
