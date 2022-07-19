with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read() #f를 읽어와서 text변수에 저장
    names = text.split('\n') # \n으로 나누어 리스트화 
    result = {} #딕셔너리 통추가
    for word in names:
        #print(word)
        if not word in result:
            result[word] = 1
        else:
            result[word] += 1

with open('03.txt', 'w', encoding='utf-8') as g:
    for dict in result:
        g.write(f'{dict} {result[dict]}\n')