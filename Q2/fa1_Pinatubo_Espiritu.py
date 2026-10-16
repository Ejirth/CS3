class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        
    def get_title(self):
        return self.__title
        
    def get_author(self):
        return self.__author
        
    def set_title(self, title):
        self.__title = title
        
    def set_author(self, author):
        self.__author = author
        
    def display_info(self):
        return f"Title: {self.__title}\nAuthor: {self.__author}"

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)  
        self.__number_of_pages = number_of_pages
        
    def get_number_of_pages(self):
        return self.__number_of_pages
        
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
            
    def display_info(self):
        parent_info = super().display_info()
        return f"{parent_info}\nPages: {self.__number_of_pages}"
        
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number
        
    def get_issue_number(self):
        return self.__issue_number
        
    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
            
    def display_info(self):
        parent_info = super().display_info()
        return f"{parent_info}\nIssue Number: {self.__issue_number}"

pub1 = Publication("Journal of Experimental Psychology", "Ratcliff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
print(pub1.display_info())

print("\nBook Information:")
book1.set_number_of_pages(-310)
print(book1.display_info())

print("\nMagazine Information:")
print(mag1.display_info())
