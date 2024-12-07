n=int(input("enter a number:"))
fact=1;
if n<0:
	print("enter a positive number")
elif n==0:
	print(f"factorial is{fact} ")
else:
	for i in range(1,n+1):
		fact=fact*i
print(f"factorial of {n} is {fact}")
