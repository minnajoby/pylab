n = int(input("Enter the upper limit (n) to display alternative prime numbers: "))

primes = []


for num in range(2, n + 1):

    is_prime = True
    

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break  
    if is_prime:
        primes.append(num)


print("Alternative prime numbers up to", n, ":")
for i in range(0, len(primes), 2):
    print(primes[i])

