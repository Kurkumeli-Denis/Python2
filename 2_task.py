#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем
# и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

a1 = int(input("Введите числитель 1 дроби:"))
b1 = int(input("Введите знаменатель 1 дроби:"))

a2 = int(input("Введите числитель 2 дроби:"))
b2 = int(input("Введите знаменатель 2 дроби:"))

if(b1 == b2):
    sum = a1 + a2
    if (sum == b2):
        print('Сумма дробей = 1')
    print('Сумма дробей =',sum,'/',b1)
else:
    c = b1 * b2
    a1 = a1 * b2
    a2 = a2 * b1
    sum = a1 + a2
    print('Сумма дробей =', sum, '/', c)
    if(sum == c):
        print('Сумма дробей = 1')
    if(c % sum == 0):
        c = c // sum
        sum = 1
        print('Сумма дробей =', sum, '/', c)
    if (sum % c == 0):
        sum = sum // c
        c = 1
        print('Сумма дробей =', sum, '/', c)

multy1 = a1 * a2
multy2 = b1 * b2
if(multy1 == multy2):
    print('Произведение дробей = 1')
print('Произведение дробей =', multy1, '/', multy2)
if(multy2 % multy1 == 0):
        multy2 = multy2 // multy1
        multy1 = 1
        print('Произведение дробей =', multy1, '/', multy2)
if(multy1 % multy2 == 0):
        multy1 = multy1 // multy2
        multy2 = 1
        print('Произведение дробей =', multy1, '/', multy2)