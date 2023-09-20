# Write your solution here


name = input("Whom should I sign this to: ")
location = input("Wher shall I save it? ")

with open(location, "w") as file: 
    file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

