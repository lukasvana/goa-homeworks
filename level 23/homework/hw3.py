num = int(input("input random number"))
num1 = int(input("input random number again"))

num2 = 0
num3 = 1

for i in range(num,num1):
    num2 = num2 + i
    num3 = num3 * i
print(num2)
print(num3)