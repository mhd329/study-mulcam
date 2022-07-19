# 'fruits.txt' 파일을 읽어와 'berry'로 끝나는 문자열을 set 타입의 변수에 기록
with open('1회차/윤혜진/data/fruits.txt', 'r', encoding='utf-8') as f:
    berrys = set()   # 과일 중복 제거
    for fruit in f:   # fruit에는 'blueberry\n'형태로 바인딩됨
        if fruit[-6:-1] == 'berry':
            berrys.add(fruit)
 
    
# '02.txt' 파일을 만든 후, 'berry'로 끝나는 문자열과 총 갯수 기록
with open('1회차/윤혜진/result/02.txt', 'w', encoding='utf-8') as f:
    f.write(str(len(berrys))+'\n')
    for berry in berrys:
        f.write(berry)
