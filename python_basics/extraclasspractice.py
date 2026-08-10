#This is just some extra class practice that I want to do

class Book:
    def __init__(self, title, author, pages, checked_out):
        self.title = title
        self.author = author
        self.pages = pages
        self.checked_out = checked_out
    def check_out(self):
        if not self.checked_out:
            print(f"You checked out {self.title}.")
            self.checked_out = True
        elif self.checked_out:
            print(f"Sorry, this book is already checked out.")
    def return_book(self):
        self.checked_out = False
        print(f"Thank you for returning {self.title}.")
    def book_info(self):
        if not self.checked_out:
            print(f"Title: {self.title}")
            print(f"Author: {self.author}")
            print(f"Pages: {self.pages}")
            print(f"Status: Available")
        else:
            print(f"Title: {self.title}")
            print(f"Author: {self.author}")
            print(f"Pages: {self.pages}")
            print(f"Status: Checked Out")


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310, False)
book2 = Book("1984", "George Orwell", 328, False)

book1.check_out()
book1.check_out()
book1.return_book()
book1.book_info()