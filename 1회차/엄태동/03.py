# 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.

with open('data/fruits.txt','r', encoding ='utf-8') as f:
    text = f.read()
    text_list=text.split()
    dic={}
    for i in text_list:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
for alphabet, num in dic.items():
    print(alphabet, num)
with open('03.txt', 'w', encoding ='utf-8') as f:
    for alphabet, num in dic.items():
        f.write(f'{alphabet}, {num}\n')