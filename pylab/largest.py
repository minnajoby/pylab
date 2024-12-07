a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third nunmber"))
if a>b and  a>c:
	print(f"{a}, is largest")
elif b>a and b>c:
	print(f"{b},is largest")
else:
	print(f"{c},is largest")
