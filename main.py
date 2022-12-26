from random import randint

# print(randint(1, 50))
name = input("Как вас зовут (только реальное имя)? : ")
print("Мы ща увидим ваши скиллы по умножению!")
n = 0
for i in range(10):
    a = randint(20, 99)
    b = randint(20, 99)
    print(f"{a} * {b} = ", end="")
    answer = int(input())
    if answer == a * b:
        n += 1
    elif n >= 5:
        print('А теперь попробуй сам (без каликульятора')
print("Game over")
print(f"Вы ответили на {n} из 10 ")