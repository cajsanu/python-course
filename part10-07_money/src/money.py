# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cent: int):
        self.__euros = euros
        self.__cents = cent

    def __str__(self):
        if self.__cents < 10:
            return f"{self.__euros}.0{self.__cents} eur"  
        if self.__cents >= 100:
            return f"{self.__euros + 1}.{self.__cents - 100:02} eur"
        return f"{self.__euros}.{self.__cents} eur"
    
    def __total(self):
        return self.__euros, self.__cents
    
    def __eq__(self, another):
        return self.__total() == another.__total()
    
    def __lt__(self, another):
        return self.__total() < another.__total()
        
    def __gt__(self, another):
        return self.__total() > another.__total()
        
    def __ne__(self, another):
        return self.__total() != another.__total()
    
    def __add__(self, another):
        new_value = self.__total() + another.__total()
        e_c = Money(new_value[0]+new_value[2], new_value[1]+new_value[3])
        return e_c
    
    def __sub__(self, another):
        total_self = self.__total()
        total_another = another.__total()
        
        euros_diff = total_self[0] - total_another[0]
        cents_diff = total_self[1] - total_another[1]
        
        if cents_diff < 0:
            euros_diff -= 1
            cents_diff += 100
            
        if euros_diff < 0 or cents_diff < 0:
            raise ValueError("Subtraction would result in a negative amount.")
        
        return Money(euros_diff, cents_diff)

        
    
        
    
    
# e1 = Money(4, 5)
# e2 = Money(2, 95)

# e3 = e1 + e2
# e4 = e1 - e2

# print(e3)
# print(e4)

# e5 = e2-e1
