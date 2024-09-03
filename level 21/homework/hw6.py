num = int(input("enter random number"))
num2 = int(input("enter second number"))

num3 = 0
for i in range(0,num):
    for a in range (0,num2):
        num3 += (a + i)
print(num3)