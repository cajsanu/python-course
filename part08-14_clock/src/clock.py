# Write your solution here:


from datetime import timedelta, datetime


class Clock:
    def __init__(self, hour, minute, second):
        self.seconds = second
        self.minutes = minute
        self.hours = hour
        self.time = datetime(1999, 2, 4, self.hours, self.minutes, self.seconds)
        self.s = timedelta(seconds=1)
        
        
    def tick(self): 
        self.time += self.s
        
    def set(self, hour, minute=0, second=0):
        self.time = datetime(1999, 2, 4, hour, minute, second)
        
    
    def __str__(self):
        return self.time.strftime("%H:%M:%S")
    
    
# clock = Clock(23, 59, 55)
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)

# clock.set(12, 5)
# print(clock)