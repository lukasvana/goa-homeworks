#შექმენით ბანკის სისტემა სადაც იქნება ძალიან ბევრი პირობები და გამოიყენებთ if, elif და else -ს, გამოიყენებთ ასევე განვლილ მასალასაც

#how much money does he have in bank

money = int(input("how much money do you have on balance: "))

#what does user  want to do

choice = input("do you want to deposit or withdraw: ")

#making withdraw machine

if choice == "withdraw":
    withdraw = int(input("how much money do you want to withdraw: "))
    balance = (money - withdraw)
    if money < withdraw:
        print("you dont have that much money on your account")
    else:
        print("you have withdrawen " + str(withdraw) + " now you have " + str(balance) + " on your account")
elif choice == "deposit":
    deposit = int(input("how much money do you want to deposit: "))
    money2 = deposit + money
    print("coonngrats you have deposited " + str(deposit) + " now you have " + str(money2))