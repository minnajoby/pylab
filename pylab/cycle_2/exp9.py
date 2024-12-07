n=int(input("enter the number of integers:"))
integer_list=[]
for i in range(n):
	integer=int(input("enter the integer:"))
	integer_list.append(integer)
result_list=[]
for num in integer_list:
	if num>100:
		result_list.append("over")
	else:
		result_list.append(num)
print("result ",result_list)

