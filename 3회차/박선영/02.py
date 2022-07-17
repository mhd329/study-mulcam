# cnt = 0
# berry = []
# with open('data/fruits.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line)
#         if line.endswith("berry"):
#             cnt += 1
#             berry.append(line)
            

#     # all = f.read()
#     # fruitlist = all.split('\n')
#     # for i in fruitlist:
#     #     print(i)
#     #     if i.endswith('berry'):
#     #         berry.append(i)

# berry = list(set(berry))
# cnt = len(berry)

# with open('02.txt', 'w', encoding='utf-8') as br:
#     br.write(f'{cnt}\n')
#     for i in berry:
#         br.write(f'{i}\n')


'''
>>> f 에 있는 내용물을 한번에 한줄씩 불러서 그 한줄당 한 번씩 조건문을 돌리려고 했음

    >>> 그 한줄 안에는 띄어쓰기도 있고 berryfake 같은 함정도 있음

        >>> 한줄(하나의 요소)를 구분할 때 띄어쓰기로 구분하는 방법은 쓸 수 없다
        >>> berryfake 때문에 if ~ in ~ 같은 방법도 쓸 수 없다.

for line in f:
    if line.endswith("~~~~"):   
    ------------------------    
        cnt += 1
        berry.append(line)
        
>>> f 가 어떤 기준으로 분리되지 않았기 때문에 line 은 f 전체
>>> txt 안의 내용물이 쪼개지지 않고 하나의 큰 덩어리 상태이기 때문에 (for 문 다음 if 문) 을 돌려도 텍스트 내용 전체에 대해서 한 번만 실행된다.
>>> 따라서 이 경우 endswith("fake") 를 하면 텍스트 마지막 줄의 내용물인 berryfake 가 나오고 cnt 는 +1 이 되며 그대로 반복 + 조건문은 종료가 된다.
        
>>> 각 줄당 strip() 을 하여 그 안에 있는 것이 조건에 맞는지 검사한다.

'''

cnt = 0
berry = []
res = []

with open ('./01.txt', 'r', encoding='utf-8') as file:
    length = int(file.read())

with open('data/fruits.txt', 'r', encoding='utf-8') as f:

    i = 0
    while i <= length: # for 문은 자체로 개행이 되서 그런가 자꾸 berry 가 들어간 문자들이 빠지는 등 오류가 나서 while 로 바꿨다...
        line = f.readline().strip()
        if line.endswith("berry"):
            berry.append(line)
        i += 1
        
    berry_list = list(set(berry))
    
    for j in berry_list:
        res.append(j)
        cnt += 1

with open('02.txt', 'w', encoding='utf-8') as br:
    
    br.write(f'{cnt}\n')
    for i in res:
        br.write(f'{i}\n')