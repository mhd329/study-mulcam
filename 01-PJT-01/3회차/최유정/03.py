# 03. 텍스트 데이터 활용 - 등장 횟수
# 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.
# Boysenberry 3
# Blueberry 4
# ...
# Melon 1
#berryfake 1

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text=f.read()
    fruits=text.split('\n')#list
    for fruit in fruits:
        fruitdic={fruit:0}
        
with open('03.txt', 'w', encoding='utf-8') as f:
    
    for key in fruitdic.keys():
        f.write(key)
        f.write('\n')