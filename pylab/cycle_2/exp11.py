n= int(input("enter the number of words:"))
word_list=[]
for i in range(n):
	word=input("enter the words:")
	word_list.append(word)
max_length=0
for word in word_list:
	length=len(word)
	if length>max_length:
		max_length=length
print("length of the longest word:",max_length)
