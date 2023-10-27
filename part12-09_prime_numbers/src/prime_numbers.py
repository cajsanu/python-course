# Write your solution here


def prime_numbers():
    n = 2
    while True: 
        if is_prime(n):
            yield n
        n += 1
        
def is_prime(number: int):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True
    
      
   
   
    
        
         
    
    
# numbers = prime_numbers()
# for i in range(8):
#     print(next(numbers))