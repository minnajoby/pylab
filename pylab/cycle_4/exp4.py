area_square = lambda side: side ** 2
area_rectangle = lambda length, breadth: length * breadth
area_triangle = lambda base, height: 0.5 * base * height
side = float(input("Enter the side length of the square: "))
print(f"Area of the square: {area_square(side)}")
length = float(input("\nEnter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
print(f"Area of the rectangle: {area_rectangle(length, breadth)}")
base = float(input("\nEnter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
print(f"Area of the triangle: {area_triangle(base, height)}")
