class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = self.validate_email(email)
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User's email has been updated.")

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def __repr__(self):
        return "User: {user}\n  Email: {email}\n  Books read: {bookCount}".format(user=self.name, email=self.email, bookCount=len(self.books))

    def __hash__(self):
        return hash((self.name, self.email))

    def read_book(self, book, rating="None"):
        self.books[book]=rating
            
    def get_average_rating(self):
        total=0
        count=0
        for n in self.books.values():
            if isinstance(n, int):
                total+=n
            count+=1
        if count == 0:
            return "No books read."
        else:
            return total/count

    def validate_email(self, email):
        at_count = email.count('@')
        ext_test = email.endswith(".com") or email.endswith(".edu") or email.endswith(".org")
        if at_count == 1 and ext_test:
            return email
        else:
            print("{e} is an invalid email.".format(e=email))
            return "Invalid Email"


class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("ISBN for {title} has been changed.".format(title=self.title))

    def add_rating(self, rating):
        if (isinstance(rating, int) or isinstance(rating, float)) and rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        return self.title == other_book.get_title() and self.isbn == other_book.get_isbn()

    def __repr__(self):
        return "Title: {title}\nISBN: {isbn}".format(title=self.title, isbn=self.isbn)

    def get_average_rating(self):
        total=0
        count=0
        for n in range(0, len(self.ratings)):
            if isinstance(self.ratings[n], int):
                total+=self.ratings[n]
            count+=1
        if count==0:
            return "No rating exists yet."
        else:
            return total/count

    def __hash__(self):
        return hash((self.title, self.isbn))



class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.get_title(), author=self.get_author())


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.get_title(), level=self.get_level(), subject=self.get_subject())




class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return self.get_book_for_book_with_isbn(book)

    def create_novel(self, title, author, isbn):
        book = Fiction(title, author, isbn)
        return self.get_book_for_book_with_isbn(book)

    def create_non_fiction(self, title, subject, level, isbn):
        book = Non_Fiction(title, subject, level, isbn)
        return self.get_book_for_book_with_isbn(book)

    def get_book_for_book_with_isbn(self, newbook):
        for book in self.books.keys():
            if book.get_isbn() == newbook.get_isbn():
                print("ISBN {i} is not unique.".format(i=book.get_isbn()))
                return book
        return newbook

    def add_book_to_user(self, book, email, rating="None"):
        found=False
        for user in self.users.values():
            if email == user.get_email():
                user.read_book(book, rating)
                book.add_rating(rating)
                found = True

        if found == False:
            print("No user with email {e}!".format(e=email))
        
        if book in self.books:
            self.books[book] += 1
        else:
            self.books[book] = 1

    def add_user(self, name, email, user_books="None"):
        user = User(name, email)
        if not user in self.users.values():
            self.users[user] = user
            print("{u} added".format(u=email))
        else:
            print("{u} already exists.".format(u=user.name))

        if isinstance(user_books, list):
            for item in user_books:
                self.add_book_to_user(item, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(user)

    def most_read_book(self):
        item = None
        count = 0
        for book, read in self.books.items():
            if read > count:
                count = read
                item = book
        return "{b} has been read {v} times.".format(b=book.get_title(), v=count)

    def highest_rated_book(self):
        item = None
        value = 0
        for book in self.books.keys():
            t = book.get_average_rating()
            if isinstance(t, float) or isinstance(t, int):
                if t > value:
                    item = book
                    value = t
        return "{book} has the highest average value of {v}.".format(book=book.get_title(), v=value)

    def most_positive_user(self):
        item = None
        value = 0
        for user in self.users.values():
            t = user.get_average_rating()
            if isinstance(t, float) or isinstance(t, int):
                if t > value:
                    item = user
                    value = t
        return "{user} has the highest average rating of {v}".format(user=user.name, v=value)

        







