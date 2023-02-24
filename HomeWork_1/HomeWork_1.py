# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print("Введите число")
num = int(input())
a = (num % 10)
b = (num % 100) // 10
c = (num % 1000) // 100
print(a + b + c)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

print("Введите число")
s = int(input())
kate = (s/3)*2
sergo = (s - kate)/2
petr = sergo
print(int(sergo), int(kate), int(petr))

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
print("Введите число")
num = int(input())
a1 = (num % 10)
b1 = (num % 100) // 10
c1 = (num % 1000) // 100
a2 = (num % 10000) // 1000
b2 = (num % 100000) // 10000
c2 = (num % 1000000) // 100000
if (a2 + b2 + c2) == (a1 + b1 + c1):
    print("Yes")
else:
    print("No")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
print("Введите число")
m = int(input())
print("Введите число")
n = int(input())
print("Введите число")
k = int(input())
if (k < m*n) and ((k % n) == 0) or ((k % m) == 0):
    print("Yes")
else:
    print("No")