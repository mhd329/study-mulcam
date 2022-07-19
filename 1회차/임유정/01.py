# 파일명을 어떤 모드로 열지 쓰고, 인코딩을 설정
# 파일객체이름을 f로 설정

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    # 텍스트는 string 타입
    count=0
    while 1 :
        if f.readline() == '' :
            break
        count+=1
    print(count)

with open('01.txt', 'w', encoding='utf-8') as f:
   print(count, file=f) # 파일 저장하기