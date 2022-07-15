# 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.

# Boysenberry 3
# Blueberry 4
# Avocado 1
# Marionberry 3
# Date 9
# ...
# Melon 1
# berryfake 1


with open('/Users/senga/Desktop/01-PJT-01/2회차/황지선/data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    list0 = text.split('\n')
    fruit = {}

    for l in list0 :
        if l in fruit :
            fruit[l] += 1
        else :
            fruit[l] = 1

    with open('03.txt', 'w', encoding='utf-8') as fi:
        for key, value in fruit.items():
            fi.write(f'{key} {value}\n')


    # fruit0 = list(zip(fruit.keys(), fruit.values()))
    # print(type(fruit0))

    # with open('03.txt', 'w', encoding='utf-8') as fi:
    #     fruit = list(fruit.items())
    #     fi.writelines(fruit)