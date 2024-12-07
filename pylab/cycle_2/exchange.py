str=input("enter a string")
if len(str)>1:
	new_str=str[-1]+str[2:-1]+str[1]
else:
	new_str=str
print(f"new string is {new_str}")
