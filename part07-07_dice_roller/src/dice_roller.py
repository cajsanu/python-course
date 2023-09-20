# Write your solution here

import random
import itertools

def roll(die: str):
    A = [3, 3, 3, 3, 3, 6]
    B = [2, 2, 2, 5, 5, 5]
    C = [1, 4, 4, 4, 4, 4]
    if die == "A":
        return random.choice(A)
    if die == "B":
        return random.choice(B)
    if die == "C":
        return random.choice(C)
    
def play(die1: str, die2: str, times: int):
    d1 = []
    d2 = []
    wins1 = 0
    wins2 = 0
    draws = 0
    for i in range(times):
        d1.append(roll(die1))
        d2.append(roll(die2))
    for (first, second) in itertools.zip_longest(d1, d2):
        if first > second:
            wins1 += 1
        elif second > first:
            wins2+= 1
        else: 
            draws += 1
    return wins1, wins2, draws



# result = play("A", "C", 3)
# print(result)
# result = play("B", "B", 3)
# print(result)