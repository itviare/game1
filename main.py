from random import randint

# print(randint(1, 50))
name = input("Как вас зовут? : ")
print("Tayor turing, hozir kara-kara tekshiramiz!")
n = 0
for i in range(10):
    a = randint(27, 95)
    b = randint(27, 95)
    print(f"{a} * {b} = ", end="")
    answer = int(input())
    if answer == a * b:
        n += 1

print("Oyin tugadi!")
print(f"Siz 10-tadan {n}-ta savolga togri javob bera oldiz")