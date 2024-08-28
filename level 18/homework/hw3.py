#თქვენით მოიფიქრეთ რაიმე სავარჯიშო რასაც გააკეთებთ if elif else ით ივარჯიშეთ დღევანდელ ნასწავლ მასალაზე ძალიან ბევრი
bread = True
cheese = False

buyer = input("what do you wnat to buy cheese bread or both: ")

if buyer== "bread":
    print("that will be 1$.")
elif buyer == "cheese":
    print("we dont have cheese right now.")
if buyer == "both":
    second_choice = input("we dont have cheese would you like to have only bread: ")
    if second_choice == "yes":
        print("that will be 1$")
    else:
        print("have a good day sir")