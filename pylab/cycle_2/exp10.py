n=int(input("enter the number of integers:"))
integer_list=[]
for i in range(n):
	integer=int(input("enter the numbers:"))
	integer_list.append(integer)
odd_list=[]
for num in integer_list:
	if num%2 !=0:
		odd_list.append(num)
print("list of odd numbers",odd_list)
