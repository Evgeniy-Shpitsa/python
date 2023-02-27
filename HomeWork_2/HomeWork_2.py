# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
print("Введите кол-во монеток")
n = int(input())
reshka = 0
orel = 0
for i in range(n):
    print("Если монета лежит орлом вверх введите 1, решкой 0")
    x = int(input())
    if x == 0:
        reshka += 1
    else:
        orel += 1
if orel > reshka:
    print(reshka)
else:
    print(orel)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
print("Введите число")
n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1