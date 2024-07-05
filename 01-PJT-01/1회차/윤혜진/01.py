# 'fruits.txt' 파일을 가져와 과일 갯수 세기
with open('1회차/윤혜진/data/fruits.txt', 'r', encoding='utf-8') as f:
    # 접근방법1
    fruit_cnt = len(f.readlines())
    # 접근방법2
    '''
    cnt = 0
    for line in f:
        cnt += 1
        print(line)
    print(cnt)
    '''  
    

# '01.txt' 파일을 생성한 후, 과일 갯수 기록
with open('1회차/윤혜진/result/01.txt', 'w', encoding='utf-8') as f:
    f.write(str(fruit_cnt))
    