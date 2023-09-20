# Write your solution here

import random

def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = list(range(lower, upper))
    drawn = list(random.sample(numbers, amount))
    return sorted(drawn)





# for number in lottery_numbers(7, 1, 40):
#     print(number)