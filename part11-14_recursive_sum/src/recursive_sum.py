# WRITE YOUR SOLUTION HERE:

def recursive_sum(number: int): 
    if number <= 1:
        return number
    return number + recursive_sum(number-1)
    
    
    
# result = recursive_sum(3)
# print(result)

# print(recursive_sum(5))
# print(recursive_sum(10))
