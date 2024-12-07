def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
def sum_series(n):
    total = 0
    for i in range(1, n + 1):
        total += (i**i) / factorial(i)
    return total
n = int(input("Enter the number of terms (n): "))
result = sum_series(n)
print(f"The sum of the series up to {n} terms is: {result}")
