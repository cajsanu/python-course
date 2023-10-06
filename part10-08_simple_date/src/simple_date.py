# WRITE YOUR SOLUTION HERE:

class SimpleDate: 
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
    def total(self):
        return self.year + self.month + self.day
        
    def __gt__(self, another):
        if self.year > another.year:
            return True
        if self.year == another.year:
            if self.month > another.month:
                return True 
            if self.year == another.year:
                if self.month == another.month:
                    if self.day > another.day:
                        return True
        return False
        
    def __lt__(self, another):
        if self.year < another.year:
            return True
        if self.year == another.year:
            if self.month < another.month:
                return True 
            if self.year == another.year:
                if self.month == another.month:
                    if self.day < another.day:
                        return True
        return False
    
    def __eq__(self, another):
        return self.total() == another.total()
    
    def __ne__(self, another):
        return self.total() != another.total()
    
    def __add__(self, number_of_days): 
        if self.day + number_of_days <= 30: 
            return SimpleDate(self.day + number_of_days, self.month, self.year)
        if self.day + number_of_days > 30:
            day = (self.day + number_of_days)%30
            month = ((self.day + number_of_days)//30) + self.month
            year = self.year
            if month > 12:
                year += month//12
                month = month%12
        return SimpleDate(day, month, year)
    
    def __sub__(self, another):
        diff_d = self.day - another.day
        diff_m = self.month - another.month
        diff_y = self.year - another.year
        
        days = (diff_y * 360) + (diff_m * 30) + diff_d
  
        return abs(days)
                
    
if __name__ == "__main__":       
        
    d1 = SimpleDate(3, 5, 1842)
    d2 = SimpleDate(1, 4, 1800)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
        