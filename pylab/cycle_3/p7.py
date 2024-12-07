n=int(input("enter the value for n:"))
integer=[]
sum=0
for i in range(1,n+1):
    if(i%6==0) and(i%4!=0):
        integer.append(i)
print(f"number in list {integer}")
for num in integer:
    sum=sum+num
print(f"sum is:{sum}")
    
