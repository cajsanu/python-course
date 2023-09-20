# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------


def older_book(book1: Book, book2: Book):
    first_book = book1.year
    second_book = book2.year
    if first_book > second_book:
        print(f"{book2.name} is older, it was published in {book2.year}")
    elif second_book == first_book:
        print(f"{book1.name} and {book2.name} were published in {book2.year}")
    else:
        print(f"{book1.name} is older, it was published in {book1.year}")
        

    
    
    
    
# python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
# everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
# norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

# older_book(python, everest)
# older_book(python, norma)