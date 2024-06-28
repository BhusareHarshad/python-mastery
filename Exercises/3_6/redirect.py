import sys

class redirect_stdout:
    def __init__(self, outfile):
        self.outfile = outfile
        
    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.outfile
        return self.outfile
    
    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout
        
        