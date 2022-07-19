#파일 내 데이터 개수
#for문을 활용, 데이터를 하나씩 읽어오며 cnt
#딕셔너리 활용해 볼것

dict = {}
with open('fruits.txt','r',encoding = 'utf-8') as f:
    for line in f:
        line = line.rstrip() 
        if line not in dict.keys() :
            dict[line] = 1 
        else:
            dict[line] += 1

print(dict)

with open('03.txt','w',encoding = 'utf-8') as f:
    for i in dict:
        f.write(f'{i} : {dict[i]}\n')
