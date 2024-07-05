# 과일 데이터 'fruits.txt' 를 활용하여 총 과일의 갯수를 '01.txt'에 기록하시오.

# 394

# fruits.txt 열기, 총 과일의 갯수 확인
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    cnt = 0
    while 1 :
        if f.readline() == '':
            break
        cnt += 1
    cnt = str(cnt)
# 파일닫기
f.close()

# 출력 파일 생성
# 생성, 내용입력, 닫기
f = open("01.txt", 'w')
f.write(cnt)
f.close()
