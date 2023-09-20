# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.list_of_numbers = []
        self.even_numbers = []
        self.odd_numbers = []

    def add_number(self, number:int):
        self.numbers += 1
        self.list_of_numbers.append(number)
        if number % 2 == 0:
            self.even_numbers.append(number)
        else:
            self.odd_numbers.append(number)

    def count_numbers(self):
        return self.numbers
    
    def get_sum(self):
        if len(self.list_of_numbers) > 0:
            return sum(self.list_of_numbers)
        else: 
            return 0
    def average(self): 
        if len(self.list_of_numbers) > 0:
            return sum(self.list_of_numbers) / len(self.list_of_numbers)
        else: 
            return 0
    def even_sum(self):
        return sum(self.even_numbers)
    def odd_sum(self):
        return sum(self.odd_numbers)
        
        
stats = NumberStats()   
print("Please type in integer numbers:")    
while True:       
    n = int(input(""))
    if n == -1:
        break
    else: 
        stats.add_number(n)

print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", stats.even_sum())
print("Sum of odd numbers:", stats.odd_sum())
