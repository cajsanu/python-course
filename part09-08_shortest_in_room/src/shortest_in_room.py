# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    
class Room:
    def __init__(self):
        self.persons = []
        
    def add(self, person: Person):
        self.persons.append(person)
        
    def is_empty(self):
        if len(self.persons) < 1:
            return True
        else:
            return False
    def print_contents(self):
        for person in self.persons: 
            print(f"{person.name} ({person.height})")
    
    def shortest(self):
        if len(self.persons) < 1:
            return None
        smallest = self.persons[0].height
        for person in self.persons:
            if person.height <= smallest:
                smallest = person.height
                shorty = person
        return shorty
    
    def remove_shortest(self):
        if len(self.persons) < 1:
            return None
        shortest = self.shortest()
        self.persons.remove(shortest)
        return shortest
        
            
if __name__ == "__main__":            
    room = Room()

    room.add(Person("Ann",120))
    room.add(Person("Tim",150))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
        
