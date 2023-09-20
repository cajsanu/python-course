# Write your solution here

import fractions

def fractionate(amount: int):
    list =[]
    for i in range(amount):
        fraction = fractions.Fraction(1, amount)
        list.append(fraction)
    return list







# for p in fractionate(3):
#     print(p)

# print()

# print(fractionate(5))

