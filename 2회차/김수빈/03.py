# 과일 데이터 fruits.txt를 활용하여 
# 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.

with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    fruits = f.read()
    fruits_list = fruits.split('\n')
    fruits_dict = {}

    for i in fruits_list:
        fruits_dict[i] = fruits_dict.get(i, 0) + 1
    # print(fruits_dict)
    for key in fruits_dict:
        print(key, fruits_dict[key])

with open('03.txt', 'w', encoding='utf-8') as f:
    for key in fruits_dict:
        f.write(f'{key} {fruits_dict[key]}\n')