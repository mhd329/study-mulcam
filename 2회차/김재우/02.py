with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    cnt = 0 # count
    berry = [] # 저장소
    for i in set(f.readlines()): # set 중복 제거
        j = (i[:-1]) # \n 개행 제거 
        if j.endswith('berry'): # 'berry'로 끝나는 단어라면 = if
            berry.append(j) # 'berry 라는 저장소에 'berry'로 끝나는 단어 append = 추가
            cnt += 1 # 'berry로 끝나는 단어 갯수 세기
    result = '\n'.join(berry) # 'berry' 서식 바꾸기
    
    print(cnt)
    print(result)
