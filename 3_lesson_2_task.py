#В большой текстовой строке подсчитать количество встречаемых слов
#и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
#За основу возьмите любую статью из википедии или из документации к языку.
import re

array = input('Введите список через пробел:')
array = re.split('[\s!?,.;:<<>>\|/]+', array)
arr = []
for i in range(len(array)):
    arr.append(array[i].lower())
print(arr)
arr2 = []
dict_1 = {}
for i in range(len(arr) - 1):
    k = 1
    for j in range(i + 1, len(arr)):
        if(arr[i] == arr[j]):
            arr[j] = 1
            k += 1
    if(arr[i] != 1):
        arr2.append(k)
        arr2.append(arr[i])
        dict_1[k] = arr[i]
print(arr)
print(arr2)
print(dict_1)

dict_1 = sorted(dict_1.items(), reverse = True)
print(dict_1)