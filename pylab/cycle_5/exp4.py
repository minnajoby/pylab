
from palindrome import is_palindrome
def find_longest_palindrome(s):
	longest=""
	for i in range(len(s)):
		for j in range(i+1,len(s)+1):
			substring=s[i:j]
			if is_palindrome(substring)and len(substring)>len(longest):
				longest=substring
	return longest
text=input("enter a string:")
result=find_longest_palindrome(text)
print("longest palindrome substring:",result)


