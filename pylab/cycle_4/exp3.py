def is_prime(num):
    
    if num < 2:
        return False
    factor_count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factor_count += 1
    return factor_count == 2 

def find_nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num


n = int(input("Enter the value of n to find the nth prime number: "))

if n <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    nth_prime = find_nth_prime(n)
    print(f"The {n}th prime number is: {nth_prime}")
