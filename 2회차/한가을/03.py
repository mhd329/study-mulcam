# 어제 8번 문제
with open('data/fruits.txt', 'r') as f:
    dict = {}

    for i in f:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

with open('03.txt', 'w', encoding = 'utf-8') as f:
    for k, v in dict.items():
        f.write(str(k) + ' ')
        f.write(str(v) + '\n')