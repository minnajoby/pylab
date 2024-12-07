import math
print(f"quadratic equation ax^2 + bx + c")
a=float(input("enter a value for a:"))
b=float(input("enter a value for b:"))
c=float(input("enter a value for c:"))
nume=(b*b)-(4*a*c)
if (nume==0):
	print("only one root is possible")
	ans=(-b)/2*a
	print(f"x1={ans}")
elif (nume>0):
	sqrtvalue=math.sqrt(nume)
	ans1=(-b+sqrtvalue)/2*a
	ans2=(-b-sqrtvalue)/2*a
	print(f"the roots are real")
	print(f"x1={ans1}")
	print(f"x2={ans2}")
else:
	print("complex number")
	sqrtvalue=math.sqrt(abs(nume))/2*a
	print(-b/(2*a),"+i", sqrtvalue)
	print(-b/(2*a),"-i", sqrtvalue)

