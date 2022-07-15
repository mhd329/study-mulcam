# 02. 텍스트 데이터 활용 - 특정 단어 추출
# - 과일 데이터 `fruits.txt`를 활용하여 `berry`로 끝나는 과일의 갯수와 목록을 `02.txt`  에 기록하시오.
#     - 과일은 하나당 한 줄에 기록되어 있습니다.
#     18

from asyncore import write


with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text=f.read()
    cnt=0
    fruitdic={}
    fruits=text.split('\n')
    
    for i in fruits:
        if i[-5:]=='berry':
            fruitdic[i]=cnt

with open('02.txt','w', encoding='utf-8') as f:
    f.write(str(len(fruitdic)))
    f.write('\n')
    for key in fruitdic.keys():
        f.write(key)
        f.write('\n')
#value값은 제대로 넣지 못했음 <key별 value값을 count하려했음