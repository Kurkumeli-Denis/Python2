#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

arr = input('Введите список через пробел:').split()
arr2 = []
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if(arr[i] == arr[j]):
            arr2.append(arr[j])
            arr[i] = 'k'
            arr[j] = 'q'

for k in range(len(arr2)):
    if(arr2[k] == 'k' or arr2[k] == 'q'):
        arr2.pop(k)
print(arr2)
