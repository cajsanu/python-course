# Write your solution here:


class Item:
    def __init__(self, name: str, weight: float):
        self.__object = name
        self.__kg = weight
        
    def name(self):
        return self.__object
    
    def weight(self):
        return self.__kg
    
    def __str__(self):
        return f"{self.__object} ({self.__kg} kg)"
    
    
class Suitcase:
    def __init__(self, max_kg: float):
        self.__max_kg = max_kg
        self.suitcase = []
        
    def add_item(self, item: Item):
            if self.weight() + item.weight() <= self.__max_kg:
                self.suitcase.append(item)
                
    def weight(self):
        comb_weight = 0
        if len(self.suitcase) > 0:
            for i in self.suitcase: 
                    comb_weight += i.weight()
        return comb_weight 
    
    def print_items(self):
        for item in self.suitcase:
            print(item)
    
    def heaviest_item(self):
        heaviest = 0
        if len(self.suitcase) > 0:
            for i in self.suitcase:
                if i.weight() > heaviest:
                    heaviest = i.weight()
                    item = i 
            return item
        else: 
            return None                   

    def __str__(self):
        if len(self.suitcase) == 1:
           return f"{len(self.suitcase)} item ({self.weight()} kg)" 
        return f"{len(self.suitcase)} items ({self.weight()} kg)"     
    
class CargoHold: 
    def __init__(self, max_weight: float):
        self.__max_weight = max_weight       
        self.__cargo = []
        
    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() <= self.__max_weight:
            self.__cargo.append(suitcase)
        
    def weight(self):
        combined_weight = 0
        if len(self.__cargo) > 0:
            for suitcase in self.__cargo:
                combined_weight += suitcase.weight()
        return combined_weight
    
    def print_items(self):
        for s in self.__cargo: 
            s.print_items()
        
                  
    def __str__(self):
        if len(self.__cargo) == 1:
           return f"{len(self.__cargo)} suitcase, space for {self.__max_weight-self.weight()} kg"
        return f"{len(self.__cargo)} suitcases, space for {self.__max_weight-self.weight()} kg"
                
            
    
if __name__ == "__main__":  
   
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
