# 과일 데이터 `fruits.txt`를 활용하여 총 과일의 갯수를 `01.txt` 에 기록하시오.
# 과일은 하나당 한 줄에 기록되어 있습니다.
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
     text = f.read()
     list = text.split('\n')
     cnt = 0
     for i in list : 
        cnt += 1
        print(cnt)

with open('01.txt', 'w', encoding="utf-8") as f2 : 
    f2.write(str(cnt))