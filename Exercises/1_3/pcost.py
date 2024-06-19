import os
with open(r'C:\Users\HARSHAD BHUSARE\Desktop\1.AdvancedPython\python-mastery\Data\portfolio.dat', 'r') as f:
    for line in f.readlines():
        name, number, cost = line.split()
        pcost = int(number)  * float(cost)
        #print(round(pcost, 2))
        with open(r'C:\Users\HARSHAD BHUSARE\Desktop\1.AdvancedPython\python-mastery\Data\portfolio_cost.dat', 'a') as f:
            t = line.replace("\n", "")
            f.write(t + " " + str(pcost) + "\n")
        
