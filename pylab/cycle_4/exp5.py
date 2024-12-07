list = []
n = int(input("Enter no. of terms: "))
for i in range(n):
    terms = int(input("Enter terms: "))
    list.append(terms)
power = lambda x: 2 ** x
power_of_2 = []
for term in list:
    power_of_2.append(power(term))
print("Powers of 2:", power_of_2)





