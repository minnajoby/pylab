n1=int(input("enter the number of colors in first  list:"))
color_list1=[]
for i in range(n1):
	color=input("enter the colors: ")
	color_list1.append(color)
n2=int(input("enter the number of colors in second list:"))
color_list2=[]
for i in range(n2):
	color=input("enter the colors:")
	color_list2.append(color)
result=[]
for color in color_list1:
	if color not in color_list2:
		result.append(color)
print(f"color from color_list 1 not contain color_list2 {result}")
