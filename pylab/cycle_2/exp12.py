n1=int(input("enter the number of integers in list"))
integer_list1=[]
for i in range(n1):
	integer=int(input("enter numbers:"))
	integer_list1.append(integer)
n2=int(input("enter the numbers of integers in list"))
integer_list2=[]
for i in range(n2):
	integer=int(input("enter the numbers:"))
	integer_list2.append(integer)
if len(integer_list1)==len(integer_list2):
	print("lists are same length")
else:
	print("list are not same length")
if sum(integer_list1)==sum(integer_list2):
	print("list sum to be same value")
else:
	print("list do not sum to be same value")
common_value=[]
for integer in  integer_list1:
	if integer in integer_list2 and integer not in common_value:
		common_value.append(integer)

if common_value:
	print(f"the common values are {common_value}")
else:
	print("there are no common values")
