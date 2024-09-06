#მომხმარებელს შემოატანინეთ რიცხვი შემდეგ while loop ის გამოყენებით 1-დან მომხმარების შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ხუთის ჯერადი რიცხვები

num = int(input("input random number:"))
num1 = 0

while num1 < num:
    if num1 % 5 == 0:
        print(num1 + 5)

    num1 = num1 + 1
