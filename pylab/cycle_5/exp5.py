import graphics.rectangle as rect
import graphics.circle as circ
import graphics.three_d_graphics.cuboid as cub
import graphics.three_d_graphics.sphere as sph
length=int(input("enter the length of rectangle:"))
breadth=int(input("enter the breadth of rectangle:"))
print("area of rectangle:",rect.area(length,breadth))
print("perimeter of rectangle:",rect.perimeter(length,breadth))

radius=int(input("enter the radius of circle:"))
print("area of circle :",circ.area(radius))
print("perimeter of circle :",circ.perimeter(radius))

length=int(input("enter the length of cuboid:"))
width=int(input("enter the width of cuboid:"))
height=int(input("enter the height of cuboid:"))

print("area of cuboid :",cub.area(length,width,height))
print("perimeter of cuboid:",cub.perimeter(length,width,height))

radius=int(input("enter the radius of sphere:"))
print("area of sphere :",sph.area(radius))
print("volume  of sphere :",sph.volume(radius))








