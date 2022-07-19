# 02. 텍스트 데이터 활용 - 특정 단어 추출

with open('data/fruits.txt', 'r', encoding='utf-8') as f:   
    lines = f.read().split('\n')
    lines = set(lines) # set = 중복요소 삭제
    cnt = 0

    for line in lines:
            if line.find("berry") > 0:           
                cnt += 1
            else:
                pass
    print(cnt)

    for line in lines:
        if line.find("berry") > 0:           
            print(line)
        else:
            pass

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write('%d\n' %cnt)

    for line in lines:
        if line.find("berry") > 0:           
            f.write('%s\n' %line)
        else:
            pass