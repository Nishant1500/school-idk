n1 = input("Enter Number 1: ")
n2 = input("Enter Number 2: ")
num1 = [str(s) for s in n1 if s.isdigit()]
num2 = [str(s) for s in n2 if s.isdigit()]

c1 = int("".join(num1))
c2 = int("".join(num2))

sum = c1 + c2
product = c1 * c2

print("Sum = " + str(sum) + "\nProduct = " + str(product))