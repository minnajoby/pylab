n=int(input("enter the number of names:"))
names=[]
for i in range(n):
	name=input("enter first names")
	names.append(name)
count=0
for name in names:
	for ch in name:
		if ch=='a':
			count+=1
print(f"total occurences of a {count}")


