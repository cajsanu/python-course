# WRITE YOUR SOLUTION HERE:

class Recording: 
    def __init__(self, length:int):
        self.__length = length 
        if self.__length < 0: 
            raise ValueError 
        
       
    @property
    def length(self):
        return self.__length
        
    @length.setter
    def length(self, len: int):
        if len > 0:
            self.__length = len
        else: 
            raise ValueError 
    
# the_wall = Recording(-1)
# print(the_wall.length)
# the_wall.length = 44
# print(the_wall.length)
