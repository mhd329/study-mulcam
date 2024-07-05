## 텍스트 데이터 활용 - 특정 단어 추출
#- 과일 데이터 `fruits.txt`를 활용하여 `berry`로 끝나는 과일의 갯수와 목록을 `02.txt`  에 기록하시오.
#   - 과일은 하나당 한 줄에 기록되어 있습니다.


with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    #names = ['berry', ' berry']
    #print(lines, type(lines))  #list
    print(lines, type(lines))

    cnt =0
    result = []

    for i in lines:
        if 'berry' in lines:
            cnt += 1
            print(cnt)


