with open('data/fruits.txt', 'r', encoding = 'utf-8') as f: # f란 이름으로 fruits.txt를 읽기 전용으로 열 건데
    text = f.read() # 이 문자열(==text) 안의
    noblank = text.replace(' ', '') # 공백을 지우고(==noblank)
    fruits = noblank.split() # 이걸 리스트로 만들어서(==fruits)

    remove = set(fruits) # fruits 내의 중복 값을 제거하고(==remove)
    reorder = list(remove) # 다시 리스트로 되돌릴 건데(==reorder)
    
    cnt = dict()
    for fruit in fruits:
        if fruit not in cnt.keys():
            cnt[fruit] = 1
        else:
            cnt[fruit] += 1
    print(cnt)