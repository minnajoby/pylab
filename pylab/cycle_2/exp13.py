str=input("enter a line:")
words=str.split()
word_count={}
for word in words:
	if word in word_count:
		word_count[word]=word_count[word]+1
	else:
		word_count[word]=1
for word,count in word_count.items():
	print(word,":",count)

