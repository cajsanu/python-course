# Write your solution here



def read_input(string:str, number1:int, number2:int):
    while True:
        try:
            user_input = int(input(string))
            if number1 <= user_input <= number2:
                return user_input
        except ValueError:
            pass

        print(f"You must type in an integer between {number1} and {number2}")


        






# number = read_input("Please type in a number: ", 5, 10)
# print("You typed in:", number)