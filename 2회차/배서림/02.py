# 과일 데이터 `fruits.txt`를 활용하여 `berry`로 끝나는 과일의 갯수와 목록을 `02.txt`  에 기록하시오.
# 과일은 하나당 한 줄에 기록되어 있습니다.


with open('data/fruits.txt', 'r', encoding = 'utf-8') as f: # f란 이름으로 fruits.txt를 읽기 전용으로 열 건데
    text = f.read() # 이 문자열(==text) 안의
    noblank = text.replace(' ', '') # 공백을 지우고(==noblank)
    fruits = noblank.split() # 이걸 리스트로 만들어서(==fruits)

    remove = set(fruits) # fruits 내의 중복 값을 제거하고(==remove)
    reorder = list(remove) # 다시 리스트로 되돌릴 건데(==reorder)

    cnt = 0 # 1) 리스트의 내의 값을 셀 건데(==cnt)
    li = [] # 2) 따로 리스트도 만들 건데(==li)
    for fruit in reorder: # reorder 안의 변수가
         if fruit.endswith('berry'): # berry로 끝나면
             cnt += 1 # 1) 수를 더해서
             li.append(fruit) # 2) 리스트에 따로 모아서
    print(cnt) # 1) cnt의 값을 출력함
    print('\n'.join(li)) # 2) li의 값을 출력함 (join 메서드==리스트를 문자열로 합쳐서 반환)


# output
# 18
# Huckleberry
# Honeyberry
# Boysenberry
# Bilberry
# Raspberry
# Strawberry
# Gojiberry
# Salalberry
# Salmonberry
# Cranberry
# Gooseberry
# Cloudberry
# Juniperberry
# Marionberry
# Blueberry
# Mulberry
# Blackberry
# Elderberry