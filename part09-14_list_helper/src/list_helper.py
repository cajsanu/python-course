# WRITE YOUR SOLUTION HERE:


class ListHelper:
    # def __init__(self):
    #     pass
    
    @classmethod   
    def greatest_frequency(cls, my_list: list):
        dic = {}
        greatest = 0
        for i in my_list:
            dic[i] = my_list.count(i)
        for k,v in dic.items():
            if v > greatest:
                greatest = v
                character = k 
        return character
    
    @classmethod
    def doubles(cls, my_list: list):
        counter = 0
        dic = {}
        for i in my_list:
            dic[i] = my_list.count(i)
        for k,v in dic.items():
            if v >= 2:
                counter += 1
        return counter
        
            
            
                
            
# numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
# print(ListHelper.greatest_frequency(numbers))
# print(ListHelper.doubles(numbers))