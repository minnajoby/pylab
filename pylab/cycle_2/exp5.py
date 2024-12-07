str=input("enter a string:")
if len(str)>=3:
	if str[-3:]=="ing":
		str=str+"ly"
	else:
		str=str+"ing"
print(f"new string is {str}")
