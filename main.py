from random import randint
import sys

# print(randint(1, 50))
name = input("Как вас зовут? : ")
if name == "Jamshid" or name == "jamshid":
    print("Даже не пытайся:))")
    sys.exit()

print("Мы можем помочь вам проверитьь ваши скиллы умножения от числа до чисвла!")
n = 0

d = int(input("Вводите 1 число"))
g = int(input("Введите 2 число"))
for i in range(10):
    a = randint(d, g)
    b = randint(d,g)
    print(f"{a} * {b} = ", end="")
    answer = int(input())
    if answer == a * b:
        n += 1

print("Игра закончилась!")
print(f"ВЫ ответили на {n} вопросов из 10!")