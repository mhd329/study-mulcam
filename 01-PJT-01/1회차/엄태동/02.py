# - 과일 데이터 `fruits.txt`를 활용하여 `berry`로 끝나는 과일의 갯수와 목록을 `02.txt`  에 기록하시오.
#     - 과일은 하나당 한 줄에 기록되어 있습니다.

with open('data/fruits.txt', 'r', encoding ='utf-8') as f:
    fruits = f.read()
    fruits_list = fruits.split("\n")
    cnt =0
    i2='berry'
    lists=''
    new_list=[]
    for i in fruits_list:
        if i2 in i:
            lists += i + ':'
            lists_list = lists.split(':')
            if i not in new_list:
                new_list.append(i)
                cnt += 1
                if i[0] == 'b':
                    new_list.remove(i)
                    cnt -= 1    
    print(cnt)
    for i in new_list:
        print(f'{i}')
with open('02.txt', 'w', encoding = 'utf-8') as f:
    f.write('18\n')
    for i in new_list:
        f.write(f'{i}\n')



