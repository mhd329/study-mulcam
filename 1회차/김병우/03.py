# 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.
 

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.read()
    fruits = fruits.split('\n')

    dic = {}

    for i in fruits:
        if dic.get(i) == None:
            dic[i] = 1
        else:
            dic[i] += 1
        print(i, str(dic[i]))

with open('03.txt', 'w', encoding='utf-8') as f:
    for k,v in dic.items():
        f.write(str(k)+" ")
        f.write(str(v)+"\n")