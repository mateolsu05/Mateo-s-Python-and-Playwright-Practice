#Below are practice exercises for Pytest:

#Exercise 1:
def test_addition():
    assert 10 + 5 == 15

def test_subtraction():
    assert 20 - 5 == 15


#Exercise 2 (Deals with testing a function):
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def test_even():
    assert is_even(4) == True

def test_odd():
    assert is_even(5) == False


#Exercise 3 (Deals with testing a class):
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

def test_rectangle():
    rectangle = Rectangle(4, 5)
    assert rectangle.area() == 20

def test_rectangle_again():
    rectangle = Rectangle(8, 2)
    assert rectangle.area() == 16