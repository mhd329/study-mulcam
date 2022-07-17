# - 과일 데이터 `fruits.txt`를 활용하여 `berry`로 끝나는 과일의 갯수와 목록을 
# `02.txt`  에 기록하시오. - 과일은 하나당 한 줄에 기록되어 있습니다.

# 구글에 startwith 검색해서 진행해보기

# fruits.txt 열기, 'berry'로 끝나는 과일 갯수 및 목록 확인

# berry 갯수 카운트하여 출력
# berry를 포함한 리시트 출력
with open('data/fruits.txt', 'r', encoding="UTF8") as data:
    contents = data.read()
#print(type(contents))
    contents = (contents.split('\n'))
    contents = list(set(contents))
    with open('02.txt', 'w', encoding='utf-8') as ff:
        s = 0
        for i in contents:
            if 'berry' in i:
                if i[-5:] == 'berry':
                   s +=1
        ff.write(f'{s}\n')

        for i in contents:
            if 'berry' in i:
                if i[-5:] == 'berry':
                    ff.write(f'{i}\n')
ff.close()