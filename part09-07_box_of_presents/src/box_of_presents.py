# WRITE YOUR SOLUTION HERE:


class Present:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        
    def __str__(self):
        return f"{self.name} ({self.weight} kg)"
    
class Box:
    def __init__(self):
        self.presents = []
        
    def add_present(self, present: Present):
        self.presents.append(present)
    
    def total_weight(self):
        comb_weight = 0
        for present in self.presents:
            comb_weight += present.weight
        return comb_weight
        
        
# book = Present("ABC Book", 2)

# box = Box()
# box.add_present(book)
# print(box.total_weight())

# cd = Present("Pink Floyd: Dark Side of the Moon", 1)
# box.add_present(cd)
# print(box.total_weight())
        
        
        