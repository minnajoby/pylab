str1=input("enter first string:")
str2=input("enter second string:")
str=str1[0:1]+str2[1:2]+str1[2:]+" "+str2[0:1]+str1[1:2]+str2[2:]
print(f"modified string is {str}")
