class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You borrowed '{self.title}' by '{self.author}'")

        else:
            print(f" '{self.title}' already borrowed ")


    def return_book(self):
        if not self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.title} has been returned")

        else:
            print(f"{self.title} was not borrowed")

b1 = Book("Python" , "Guido van Rossum")
b2 = Book("Java" , "James")

b1.borrow()
b1.borrow()
b1.return_book()
b1.return_book()

            
