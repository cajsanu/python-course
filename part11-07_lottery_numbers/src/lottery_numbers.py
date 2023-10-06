# WRITE YOUR SOLUTION HERE:


class LotteryNumbers:
    def __init__(self, week_nr: int, seven_nrs: list):
        self.week_nr = week_nr
        self.seven_nrs = seven_nrs
        
    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.seven_nrs])
    
    def hits_in_place(self, numbers: list):
        return [number if number in self.seven_nrs else -1 for number in numbers]
        
        
        
        
# week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
# my_numbers = [1,4,7,10,11,20,30]

# print(week8.hits_in_place(my_numbers))
        
        
        