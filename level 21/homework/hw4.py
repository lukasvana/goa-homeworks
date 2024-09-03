#მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე შეამოწმებ რიცხვი ლუწია თუ კენტი დაბეჭდეთ რიცხვები და თან გვერძე მიუწერეთ ლუწია თუ კენტი

num = int(input("input a random number:"))
for i in range(1,num):
        if  i % 2:
            print(str(i) + " luwia")
        else:
            print(str(i) + " kentia")