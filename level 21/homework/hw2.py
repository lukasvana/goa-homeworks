#მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაითვალეთ ამ რიცხვამდე ყველა ნატურალური რიცხვის ჯამი
num2 = 0

num = int(input("input a random number:"))
for i in range(1,num):
    num2 += i
print(num2)