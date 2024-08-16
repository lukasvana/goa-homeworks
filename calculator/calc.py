#making calculator

print("this is calculator.")

#inputting first input

first = input("first number:")

#inputting second number

second = input("second number:")

#inputting what does user want to do with numbers

print("type it in numbers!!!")
print("1.add them")
print("2.subtract them")
print("3.multiply them")
print("4.devide them")

math = input("what do you want to do with this numbers")

#making calculations

if(math == "1"):
    print(int(first) + int(second))
if(math == "2"):
    print(int(first) - int(second))
if(math == "3"):
    print(int(first) * int(second))
if(math == "4"):
    print(int(first) / int(second))