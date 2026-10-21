# book_dict = {
#     "title":"Кобзар",
#     "author":"Шевченко",
#     "copies":15
# }
# print(book_dict["title"])

# class book:
#     def __init__(self,title,price, copies):
#         self.title = title
#         self.price = price
#         self.copies = copies
#
#     def avialable(self):
#         return self.copies > 0
# book1 = book("Кобзар", 300, 15)
# book2 = book("Лісова пісня", 500, 7)
# print(book1.title, book1.price)
# print(book2.title, book2.price)
# print(f"Кобзар доступний: {book1.avialable()}")
# print(f"Лісова пісня доступна: {book2.avialable()}")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)
    def area(self):
        return self.width * self.height
    def info(self):
        print(f"Розміри прямокутника: {self.width} x {self.height}")
        print(f"S={self.area()}")
        print(f"P={self.perimeter()}")

a = int(input())
b = int(input())
rectangle = Rectangle(a, b)
rectangle.info()