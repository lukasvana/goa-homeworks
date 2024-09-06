#პითონში აქამდე რაც კი გვისწავლია ყველაფრის გამოყენებით გააკეთეთ მაქსიმალურად დახვეწილი რეგისტრაციის ფუნქციონალი, ეცადეთ რაც შეიძლება დახვეწოთ და გააუმჯობესოთ დაუმატოთ ბევრი ფუნქციონალები და ასე შემდეგ, აუცილებლად გამოიყენეთ ლუპები

choice = input("do you want to registar or sign in:")
if choice == "register":
    name = input("username:")
    password = input("password:")
    birth_date = input("date of birth:")
    gender = input("gender:")
    print("account created sucsessfully")
elif choice == "sign in":
    name2 = input("username:")
    while name2 != "mayvala":
        name2 = input("incorrect try again:")
    pas_info = input("did you forgot your password:")
if pas_info == ("yes"):
    import random
    print("this is youre code:")
    list =[1023,4567,2345,6789,3456,7890,4567,8901,5678,9012,6789,7890,1234,8901,2345,9012,3456,1234,5678,1357,2468,2468,3579,3579,4680,4680,5791,5791,6802,6802,7913,7913,8024,8024,9135,9135,1357,1987,6543,5678,1234,8765,4321,3456,4321,7890,5678,2345,9876,6789,5432,8901,6789,1234,9876,2345,6789,3456,7890,4567,8901,5678,9012,6789,7890,1234,9012,3456,4567,1234,6789,2345,7890,3456,8901,4567,9012,5678,6789,1234,7890,2345,8901,3456,9012,4567,5678,1234,6789,2345,7890,3456,8901,5678,6789,1234,7890,2345,8901,3456,9012,4567,5678,1357,4680,2468,5791,3579,6802,4680,7913,5791,8024,6802,9135,7913,8024,1357,9135,2468,3579,1357,4680,2468,5791,3579,6802,4680,7913,5791,8024,6802,9135,7913,8024,1357,9135,2468,3579,1357,4680,2468,5791,3579,6802,4680,7913,5791,8024,6802,9135,7913,8024,1357,9135,2468,3579,1357,4680,2468,5791,3579,6802,4680,7913,5791,8024,6802,9135,7913,8024,1357,9135,2468,3579,1357,4680,2468,5791]
    code = random.choice(list)
    print(code)
    password3 = int(input("enter your code:"))
    while password3 != code:
        password3 = int(input("incorrect code try again:"))
    print("corect code your password is mayvala123")
    password2 = input("password:")
    while password2 != ("mayvala123"):
        password2 = input("incorrect try again:")
    print("sucsessfully logged in")