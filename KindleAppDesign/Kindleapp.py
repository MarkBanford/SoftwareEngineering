'''Online Cloud reading platform coderpad
Need helping to design (OOD)
Users have a library of books that they can add or remove
Users can set a book from their library as active
The app remembers the last page the reader was on
The app only displays a page of text at a time in the active book


Classes:
    - Book Class
        -id [int]
        -title:[str]
        -pages/content in the book: [list] as list is ordered just like a book
         -last page read [int] (remember off-by-one error) as list start at zero, books start at 1
    - Library Class
        -collection of books: {id:Book()}
        -active book : correspond to id

'''


class Book:
    def __init__(self, id, title, content):
        self.title = title
        self.content = content
        self.last_page = 0
        self.id = id

    def display_page(self):
        return self.content[self.last_page]

    def turn_page(self):
        self.last_page += 1
        return self.display_page()


class Library:
    def __init__(self):
        self.collection = dict()
        self.active_book = None
        self.id_counter = 0

    def add_to_collection(self, title, content):
        new_book = Book(self.id_counter, title, content)
