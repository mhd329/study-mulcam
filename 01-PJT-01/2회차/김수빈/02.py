# 과일 데이터 fruits.txt를 활용하여 
# berry로 끝나는 과일의 갯수와 목록을 02.txt에 기록하시오.

with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    fruits = f.read()
    fruits_list = fruits.split('\n')
    cnt = 0

    for i in set(fruits_list):
        if i.endswith('berry'):
            print(i)
            cnt += 1
    print(cnt)

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(str(cnt) + '\n')
    for i in set(fruits_list):
        if i.endswith('berry'):
            f.write(f'{i}\n')