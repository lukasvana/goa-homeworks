#მომხმარებელს შემოატანინეთ რიცხვი შემდეგ while loop ის გამოყენებით 1-დან მომხმარების შემოტანილ რიცხვამდე დაბეჭდეთ ყველა რიცხვი და თან გვერძე მიუწერეთ ლუწია თუ კენტი


num = int(input("input randeom number:"))
num1 = 0


while num1 < num:
    if num1 % 2 == 0:
        print(str(num1) + "luwia")
    else:
         print(str(num1) + "kentia")
    
    num1 = num1 + 1