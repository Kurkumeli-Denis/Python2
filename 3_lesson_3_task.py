#Создайте словарь со списком вещей для похода в качестве ключа и
# их массой в качестве значения. Определите какие вещи влезут в рюкзак передав
# его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

dict_travel = {3: 'вода', 2: 'спальник', 5: 'еда', 1: 'одежда'}
x = int(input('Грузоподъемность рюкзака:'))
dict_travel = sorted(dict_travel.items(), reverse = True)

new_dict={}

for k in dict_travel:
    if(x >= k[0]):
        x = x - k[0]
        new_dict[k[0]]=k[1]

print(new_dict)