# 1
# lst = [1, 5, 2, 1, 4, 5]
# l1 = []
# for elem in lst:
#     if elem not in l1:
#         l1.append(elem)
# print(l1)

# 2
# lst = [1, 5, 2, 1, 4, 5, 5]
# count = 0
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j]:
#             count += 1
# print(count)

# 3

# C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# if sum(C_1) > sum(C_2):
#     print(f'сумма больше в кортеже {C_1}')
# elif sum(C_2) > sum(C_1):
#     print(f'сумма больше в кортеже {C_2}')
# else:
#     print('суммы равны')

# 4
# s = 'An apple a day keeps the doctor away'
# d = {symbol: s.count(symbol) for symbol in s}
# print(d)

# 5

d = {
    "торт": [['мука','яйца','сливки','вишня'], 2.50, 200],
    "кекс": [['мука','яйца','изюм','масло'], 2.0, 150],
    "рулет": [['крем','яйца','какао','клубника'], 2.50, 200]
}
while True:
    menu = input('''1. Описание
    2. Цена
    3. Количество
    4. Вся информация
    5. Выход''')
    if menu == "Выход":
        break
    if menu == 'Описание':
        print(d.keys())
    if menu == 'Цена':
        desert = input('Выберете десерт')
        if desert in d:
            print()
    if menu == 'Количество':
        print()
    if menu == 'Вся информация':
        print()



# 6

# lst1 = [1, 5, 8, 5, 2, 5]
# lst2 = [5, 2, 9]
# print(len(lst1) + len(lst2))

# 7

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("ZeroDivisionError")

# 8 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# kr = open('kr.txt', 'r', encoding='utf-8')
# kr.write('Василюк 4')
# kr.write('Иванов 2')
# kr.write('Петров 5')
# kr.write('Сидоров 3')
