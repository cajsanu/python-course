# Write your solution here

def  new_person(name: str, age: int):
    if name == "" or len(name.split(" ")) < 2 or len(name) > 40 or age < 0 or age > 150:
        raise ValueError("Not valid")
    else:
        return(name, age)
    