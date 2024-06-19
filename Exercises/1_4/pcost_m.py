def readfile(filename):
    pcost = []
    with open(filename, "r") as f:
        for line in f.readlines():
            try:
                name, number, cost = line.split()
                pcost.append(int(number) * float(cost))
            except ValueError as ve:
                print(f"Unable to process for {name} due to {ve}")
                
    tot = sum(pcost)
            
    return tot

print(readfile(r'C:\Users\HARSHAD BHUSARE\Desktop\1.AdvancedPython\python-mastery\Data\portfolio2.dat'))
            