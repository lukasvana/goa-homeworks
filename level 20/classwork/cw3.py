#1-დან 100-მდე დაითვალეთ ხუთის ჯერადი რიცხვების ჯამი გამოიყენეთ if, else გამოგადგებათ % ნიშანი

mayvala = 0

for i in range(1,100):
    if i % 5 == 0:
        mayvala += i
print(mayvala)