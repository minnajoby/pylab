def compare(S1, S2, n):
    return S1[:n] == S2[:n]
S1 = input("Enter the first string (S1): ")
S2 = input("Enter the second string (S2): ")
n = int(input("Enter the number of characters to compare (n): "))
result = compare(S1, S2, n)
print("The first", n, "characters are the same:", result)
