# find area and perimeter of rectangle
# 1. Enter length of rectangle in centimeter
# 2. Enter breadth of rectangle in centimeter

class Rectangle():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(self.length*self.breadth, 'sq cm\n')

    def perimeter(self):
        print(2*(self.length+self.breadth, 'cm'))

length_of_rectangle  = float(input("Enter length of rectangle in cm="))
breadth_of_rectangle = float(input("Enter breadth of rectangle in cm="))

rect = Rectangle(length_of_rectangle,breadth_of_rectangle)

print("\nAREA OF RECTANGLE IS = ")
rect.area()

print("\nPERIMETER OF RECTANGLE IS = ")
rect.perimeter()
