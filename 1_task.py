# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление.
# Функцию hex используйте для проверки своего результата.

x = int(input("Введите целое число:"))
y = hex(x)
print('Проверка с помощью HEX =',y)
arr = []
if(x < 16):
    arr.append(x)
while x >= 16:
    res = x % 16
    #print(res)
    res2 = x // 16
    #print(res2)
    arr.append(res)
    x = res2
    if (x < 16):
        arr.append(x)
    if (x == 16):
        arr.append(1)

arr.reverse()


for i in range(len(arr)):
    if (arr[i] == 10):
        arr[i] = 'A'
    if (arr[i] == 11):
        arr[i] = 'B'
    if (arr[i] == 12):
        arr[i] = 'C'
    if (arr[i] == 13):
        arr[i] = 'D'
    if (arr[i] == 14):
        arr[i] = 'E'
    if (arr[i] == 15):
        arr[i] = 'F'
print('Мой ответ =',arr)