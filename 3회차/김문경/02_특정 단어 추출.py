from unicodedata import name

# readlines로 읽으면 리스트로 반환하고 뒤에 개행문자가 다 포함돼있음
# 그래서 반복문 돌려서 strip으로 공백을 다 제거하고
# endswith 조건을 만족하면 빈 리스트에 차례대로 append
# 중복 요소들은 리스트를 set으로 변환시키면 됨!

with open('fruits.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    name_list = []
    for line in lines:
        line = line.strip()
        if line.endswith('berry'):
            name_list.append(line)

    with open('02.txt', 'w', encoding='utf-8') as f:
        f.write(f'{len(set(name_list))}\n')
        for i in set(name_list):
            f.write(f'{i}\n')

