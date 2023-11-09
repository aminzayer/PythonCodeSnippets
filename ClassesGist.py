# Class representing a Car
class Car:

    def __init__(self, make, model, year):
        """
        Constructor to initialize the car object with make, model, and year.

        :param make: The make of the car (e.g., Toyota, Ford)
        :param model: The model of the car (e.g., Camry, Mustang)
        :param year: The manufacturing year of the car
        """
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0  # Initial speed is set to 0

    def accelerate(self, acceleration):
        """
        Method to accelerate the car.

        :param acceleration: The amount by which the car should accelerate
        """
        self.speed += acceleration
        print(f"The car is accelerating. Current speed: {self.speed} mph")

    def brake(self, deceleration):
        """
        Method to apply brakes and decelerate the car.

        :param deceleration: The amount by which the car should decelerate
        """
        self.speed -= deceleration
        if self.speed < 0:
            self.speed = 0
        print(f"The car is braking. Current speed: {self.speed} mph")


# Example usage of the Car class
my_car = Car("Toyota", "Camry", 2022)
print(f"My car: {my_car.year} {my_car.make} {my_car.model}")

my_car.accelerate(20)
my_car.brake(10)


# Class representing a Book
class Book:

    def __init__(self, title, author, ISBN):
        """
        Constructor to initialize the book object with title, author, and ISBN.

        :param title: The title of the book
        :param author: The author of the book
        :param ISBN: The ISBN (International Standard Book Number) of the book
        """
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_checked_out = False  # Initial state: not checked out

    def __str__(self):
        """
        String representation of the book.

        :return: A string representation of the book
        """
        return f"{self.title} by {self.author} (ISBN: {self.ISBN})"


# Class representing a Library
class Library:

    def __init__(self):
        """
        Constructor to initialize the Library object with an empty book catalog.
        """
        self.catalog = []

    def add_book(self, book):
        """
        Method to add a book to the library catalog.

        :param book: The book object to be added
        """
        self.catalog.append(book)
        print(f"Book added to the library: {book}")

    def check_out_book(self, ISBN):
        """
        Method to check out a book from the library.

        :param ISBN: The ISBN of the book to be checked out
        """
        for book in self.catalog:
            if book.ISBN == ISBN and not book.is_checked_out:
                book.is_checked_out = True
                print(f"Book checked out successfully: {book}")
                return
        print(f"Book with ISBN {ISBN} not found or already checked out.")


# Example usage of the Library Management System
library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")

library.add_book(book1)
library.add_book(book2)

library.check_out_book("978-0743273565")
library.check_out_book("978-0743273565")  # Try to check out the same book again
