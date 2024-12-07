number=[-15,-3,-1,4,6,7,0]
positive_num=[]
for num in number:
	if num>0:
		positive_num.append(num)
print(f"positive numbers are {positive_num}")
n=6
squre_num=[]
for num in range(1,n+1):
	squre_num.append(num**2)
print(f"squares of numbers{squre_num}")
word='helloword'
vowel=[]
for char in word:
	if char in 'aeiouAEIOU':
		vowel.append(char)
print(f"list of vowels are {vowel}" )
ordinal_values=[ord(char)for char in word]
print(f"ordinal values are {ordinal_values}")
