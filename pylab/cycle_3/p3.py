n=int(input("enter the size of list:"))
number_list=[]
if n<0:
	print("enter a valid number")
else:
	for i in range (n):
		number=int(input("enter the numbers:"))
		number_list.append(number)
print(f"numbers in the list are:")

print(f"{number_list}")
sum=0
for num in (number_list):
	sum=sum+num
print(f"sum of numbers in the list is {sum}")
