<<<<<<< HEAD
=======
##- 과일 데이터 `fruits.txt`를 활용하여 `berry`로 끝나는 과일의 갯수와 목록을 `02.txt`  에 기록하시오
##  한 줄씩 읽습니다.

>>>>>>> 6cb3752de837207a52ee476bb4a4abebc19c0b6f
with open("data/fruits.txt", 'r', encoding='utf-8') as f:
    a=f.readlines()
    print(a)
    cnt=0
<<<<<<< HEAD
    c=[]
=======
    b=[]
>>>>>>> 6cb3752de837207a52ee476bb4a4abebc19c0b6f
    a=set(a)
    for i in a:
        k = i[:-1]
        if k.endswith('berry'):
            cnt+=1
<<<<<<< HEAD
            c.append(i)
print(cnt)   
with open("02.txt", 'w', encoding='utf-8') as fw:
    fw.write(f'{cnt}\n')
    for j in c:
=======
            b.append(i)
print(cnt)   
with open("02.txt", 'w', encoding='utf-8') as fw:
    fw.write(f'{cnt}\n')
    for j in b:
>>>>>>> 6cb3752de837207a52ee476bb4a4abebc19c0b6f
        print(j)
        fw.write(j)