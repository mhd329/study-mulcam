# 과일 데이터 `fruits.txt`를 활용하여 `berry`로 끝나는 
# 과일의 갯수와 목록을 `02.txt`  에 기록하시오.
# 과일은 하나당 한 줄에 기록되어 있습니다.
new_list = []

with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    cnt = 0
    for i in f:
        i = i.rstrip('\n')
        if i[-5:] == 'berry':
            if i not in new_list:
                new_list.append(i)
                print(i)
                cnt += 1
print(cnt)
    # berry_count = f.count('berry')
    # print(berry_count)