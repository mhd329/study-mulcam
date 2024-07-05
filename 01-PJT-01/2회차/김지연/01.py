# 01. 텍스트 데이터 입력

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
# 파일명, 모드, 인코딩 설정
    lines = f.read().split('\n')
    # readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다. 
    cnt = 0
    for line in lines:
        cnt += 1
print(cnt)

with open('01.txt', 'w', encoding='utf-8') as f:
    f.write('%d' % cnt)