str=input("enter a string")
first_character=str[0]
for i in range(1,len(str)):
	if str[i]==first_character:
		first_character+="$"
	else:
		first_character+=str[i]
print(f"new string is {first_character}")
