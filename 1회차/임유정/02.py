# 과일 데이터 `fruits.txt`를 활용하여 `berry`로 끝나는 과일의 갯수와 목록을 `02.txt`  에 기록하시오.
# 과일은 하나당 한 줄에 기록되어 있습니다.


with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    count=0
    for i in readline() :
        if i[::-5] = 'berry'
        if f.readline() == '' :
            break
        count+=1
    print(count)