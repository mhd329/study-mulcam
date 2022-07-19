num=0
with open('data/fruits.txt','r',encoding='utf-8')as f:
    for line in f:
        num+=1
        print(line, end='')
    print(f'\n{num}')
    '''
    a='jojoj'
with open('a.txt', 'w',encoding='utf-8')as f:
    f.write(a)'''
'''- 과일 데이터 `fruits.txt`를 활용하여 총 과일의 갯수를 `01.txt`  에 기록하시오.
    - 과일은 하나당 한 줄에 기록되어 있습니다.
    '''