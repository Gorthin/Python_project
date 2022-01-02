import random

myNumbers = []
while len(myNumbers) < 7:
    newNumbers = random.randint(1,49)
    if newNumbers in myNumbers:
        print("Eliminated: ", newNumbers)
        continue
    myNumbers.append(newNumbers)
print("Those numbers will win:" ,myNumbers)