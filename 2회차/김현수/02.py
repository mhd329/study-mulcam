
with open('data/fruits.txt', 'r', encoding='utf-8') as f: #fruilts.txt 읽기
    text = f.read()
    #print(text, type(text))
    names = text.split('\n') 
    names = list(set(names)) #세트로 변환하여 같은값 제거 후 다시 리스트로 변환
    #print(names, type(names))
    count = 0
    berry = 'berry'
    berry_name = ''
    
    for name in names:
        for i in range(1,6):
            if berry[-i] != name[-i]: #끝이 berry로 끝나는지 하나씩 확인 name.startswith('berry')같이 활용
                break
        else:
            count += 1
            berry_name += name + '\n'
            
with open('02.txt', 'w', encoding='utf-8') as g:
     g.write(f'{count}\n')
     g.write(berry_name)
