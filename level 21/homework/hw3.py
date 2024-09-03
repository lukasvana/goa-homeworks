#მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაითვალეთ მომხმარებლის შემოტანილ რიცხვამდე რიცხვების საშუალო არითმეტიკული
num1 = 0
num2 = 0

num = int(input("input a random number:"))
for i in range(1,num):
    num2 += i
    num1 += 1

num3 = num2/num1

print(num3)