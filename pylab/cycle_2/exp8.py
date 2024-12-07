color=input("enter colors seperated by commas")
color_list=color.split(",")
for i in range (len(color_list)):
	color_list[i]=color_list[i].strip()
print("first color:",color_list[0])
print("second color:",color_list[-1])
