n=int(input("enter the number of tearms in fibnocci series:"))
first_num=0
second_num=1
if n<0:
	print("enter a positive number")
elif n==1:
	print(f"fibnocci series upto 1 term is {first_num}")
else:
	print(f"fibnocci series upto {n} is:")
print(first_num)
for i in range (1,n):
	print(second_num)
	num=first_num+second_num
	first_num=second_num
	second_num=num
