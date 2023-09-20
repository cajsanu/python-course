# Write your solution here

import random
import string

def generate_password(amount: int):
    letters = string.ascii_lowercase
    password = random.sample(letters, amount)
    return "".join(password)


# for i in range(10):
#     print(generate_password(2))