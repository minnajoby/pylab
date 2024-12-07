num = input("Enter a number: ")
reversed_num = num[::-1]
if num == reversed_num:
    print(f"{num} is a palindromic number.")
else:
    print(f"{num} is not a palindromic number.")
