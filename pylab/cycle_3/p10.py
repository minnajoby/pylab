num = int(input("Enter number: "))
number = []
i = 1
while i <= num:
    if num % i == 0:
        number.append(i)
    i =i+1
print(f"Factors of {num} are: {number}")
