# 01. 텍스트 데이터 입력 (연습)
# - 과일 데이터 `fruits.txt`를 활용하여 총 과일의 갯수를 `01.txt`  에 기록하시오.
#     - 과일은 하나당 한 줄에 기록되어 있습니다.
#     394



from base64 import encode


with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text=f.read()
    #print(text)
    
    fruits=text.split('\n')
    cnt=len(fruits)
with open('01.txt','w', encoding='utf-8') as f:
    
    f.write(str(cnt))

#cnt가 계속 436이 나옴>>split()했더니 공백으로 분리해서 cnt됐음...ex Juniper berry> juniper/berry로