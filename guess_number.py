from random import randint

number = randint(1, 100)
print('Угадай число от 1 до 100')

while True:
    guess = int(input('Введите число: '))

    if guess < number:
        print('Ваше число меньше того, что загадано.')

    elif guess > number:
        print('Ваше число больше того, что загадано.')

    elif guess == number:
        # ...прерываем выполнение программы и...
        break
# ...выводим сообщение.
print('Отличная интуиция! Вы угадали число :)')