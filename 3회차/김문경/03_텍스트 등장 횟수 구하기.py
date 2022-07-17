# 전체 파일을 read()로 읽어올 수도 있고 readlines으로도 가능
# readlines로 가지고오면 리스트 형태로 반환하며 각 요소 끝에 개행문자가 있음
# split로 지워주고 반복문 계속 돌림
# 딕셔너리 안에 키가 있으면 그 키에 해당하는 값에 +1, 없으면 새로 1이라는 값을 가지는 키-값 쌍을 추가

with open('fruits.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    my_dict = {}
    for line in lines:
        line = line.strip()
        if line in my_dict:
            my_dict[line] += 1
        else:
            my_dict[line] = 1
    with open('03.txt', 'w', encoding='utf-8') as f:
        for i in (my_dict):
            f.write(f'{i} {my_dict[i]}\n')
