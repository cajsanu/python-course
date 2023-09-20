# Write your solution here:
from datetime import timedelta, datetime


class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.time = datetime(1999, 1, 1, 0, self.minutes, self.seconds)
        self.s = timedelta(seconds=1)
        
        
    def tick(self): 
        self.time += self.s
    
    def __str__(self):
        return self.time.strftime("%M:%S")
    


# watch = Stopwatch()
# for i in range(3600):
#     print(watch)
#     watch.tick()