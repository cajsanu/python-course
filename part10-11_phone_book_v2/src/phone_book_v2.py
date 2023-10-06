
# Write your solution here:


class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []  
        self.__addresses = []  

    def name(self):
        return self.__name

    def add_number(self, number: str):
        self.__numbers.append(number)

    def numbers(self):
        return self.__numbers

    def add_address(self, address: str):
        self.__addresses.append(address)

    def address(self):
        if len(self.__addresses) < 1:
            return None
        return self.__addresses[0]
    
    def __str__(self):
        return f"{self.__name}\n{', '.join(self.__numbers)}\n{', '.join(self.__addresses)}"
    
    
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)
        
    def add_address(self, name: str, address: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)
                
    def get_entry(self, name: str):
        if name not in self.__persons:
            return None
        return self.__persons[name]
        
    def all_entries(self):
        return self.__persons
    
    def __str__(self):
        return f"{self.__persons}"
            

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        person_or_none = self.__phonebook.get_entry(name)
        if person_or_none == None:
            print("number unknown")
            print("address unknown")
            return 
        elif len(person_or_none.numbers()) < 1:
            print("number unknown")
        elif person_or_none.address() is None:
            print("address unknown")
        print(person_or_none)  
            
    def add_address(self):
        name = input("name: ")
        address = input("Address: ") 
        self.__phonebook.add_address(name, address)    

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


application = PhoneBookApplication()
application.execute()

