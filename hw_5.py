# 1.Дано число n. Вывести все числа от 1 до n.
i = 0
n = int(input())
while i < n:
    i += 1
    print(i)

# 2.Дано число n. Посчитать сумму всех чётных чисел от 0 до n.

i = 0
n = int(input())
sum = 0
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)

# 3.Дано натуральное число. Определить произведение цифр в нем которые кратны 2, кроме числа 0.

n = int(input())
multiply = 1
while n > 0:
    a = n % 10
    if a % 2 == 0:
        multiply *= a
    n = n // 10
print(multiply)

# 4. Дано число n. Вывести на экран числа 1, 4, 9, 16, 25, ... которые меньше n.
# Sample Input :
# 15
# Sample Output :
# 1 4 9

n = int(input())
i = 0
for i in range(1, n + 1):
        if i ** 2 <= n:
                print(i**2)

n = int(input())
i = 0
while i <= n:
        if i ** 2 <= n:
                print(i ** 2)
        i += 1


# 5. Дано число n. Среди чисел 1, 4, 9, 16, 25, ... найти первое, которые больше n.
# Sample Input :
# 5
# Sample Output :
# 9

n = int(input())
i = 1
while i * i <= n:
        i += 1
print(i * i)

# Дано число n. Определить первую цифру этого числа.
# Дано число n. Найти сумму цифр в этом числе.
# Дано натуральное число n. Найти значение минимальной цифры в данном числе .
