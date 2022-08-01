# 1. С клавиатуры вводится 7 значное число. Если четных цифр в нем больше, чем
# нечетных, то найти сумму всех его цифр, если нечетных больше, то найти
# произведение 1 3 и 6 цифры.
n = int(input())
numbers = [n // 1000000, (n // 100000) % 10, (n // 10000) % 10, (n // 1000) % 10, (n // 100) % 10, (n // 10) % 10,
           n % 10]
chet = 0
nechet = 0
for number in numbers:
    if number % 2 == 0:
        chet += 1
    else:
        nechet += 1
if chet > nechet:
    print(sum(numbers))
else:
    print(numbers[0] * numbers[2] * numbers[5])


# 2. С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько
# согласных. В случае равенства вывести на экран все гласные буквы.

s = input()
glas = 0
sogl = 0
for i in s:
    if i.isalpha():
        letter = i.lower()
        if letter == "a" or letter == "e" or\
           letter == "i" or letter == "o" or\
           letter == "u" or letter == "y":
            glas += 1
        else:
            sogl += 1
print(f'гласных - {glas} согласных - {sogl}')

3. Вводится 2 числа с клавиатуры (от 1 до 20). Так же генерируется 2 числа рандомно.
Посчитать, сколько раз пара введенных чисел с клавиатуры окажется больше
рандомной пары. Проверку выполнить 7 раз.
В случае равенства (количества, когда пара больше и всех остальных случаем)
вывести случайные числа, полученные в 4 итерации.

import random
s = 0
number3 = number4 = 0
for i in range(1, 8):
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    print(number1, number2)
    number3, number4 = map(int, input().split())
    if number1 + number2 < number3 + number4:
        s += 1
    if i == 4:
        number1, number2 = number3, number4
if s >= 4:
    print(number3, number4)

# 4. Посчитать, сколько раз встречается определенная цифра в числах. Количество
# введенных чисел и искомая цифра задаются с клавиатуры. Числа выбираются
# рандомно.

import random

n = int(input("Сколько чисел? "))
d = int(input("Какая цифра? "))
count = 0
for i in range(1, n + 1):
    m = random.randint(1, 100)
    print(m)
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10
print(f"Было введено {count} цифр {d}")

# 5. Вводится строка, содержащая буквы, целые неотрицательные числа и иные символы.
# Требуется все числа, которые встречаются в строке отдельно вывести на экран. Строка
# может содержать пробелы.

s = input()
s1 = ''
for i in range(len(s)):
    if s[i].isdigit():
        s1 += s[i]
    if s[i] == ' ':
        s1 += s[i]
    i += 1
print(s1)

# 6. Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в
# веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а
# также сколько всего букв в слове, сколько гласных и согласных

s = input()
lower_letter = 0
upper_letter = 0
for i in range(len(s) - 1):
    if s[i].islower() and s[i + 1].islower():
        lower_letter += 1
    elif s[i].isupper() and s[i + 1].isupper():
        upper_letter += 1
print(lower_letter, upper_letter)
