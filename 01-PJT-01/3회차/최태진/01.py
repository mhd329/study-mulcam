#파일에 있는 문자열 개수 찾기
#파일을 열고 1줄마다 cnt 1증가
#총 갯수 출력
cnt = 0
with open('fruits.txt','r', encoding = 'utf-8') as f:
    for line in f:  #i가 f에 저장된 데이터를 줄 단위로 읽어옴
        cnt += 1
    print(cnt)