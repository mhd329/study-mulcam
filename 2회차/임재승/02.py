f = open('./data/fruits.txt', 'r', encoding='UTF8')

lines = f.readlines()
# set과 list를 활용해서 중복을 제거해준다.
set_lines = list(set(lines))
# 개행을 삭제한 리스트를 만들어준다.
fruits = [fruit.strip() for fruit in set_lines]
print(set_lines)


def find_berry(n):
    # berry를 카운트할 변수와 berry를 담아줄 리스트변수를 선언한다.
    berry_count = 0
    berry_index = []
    
    for idx in range(0, len(n)):
        # berry라는 단어로 끝날때 True를 반환
        if n[idx].endswith('berry'):
            berry_count += 1
            #
            berry_index.append(n[idx].replace('\n', ''))
    
    # 선언한 변수 프린트
    print(berry_count)
    print(*berry_index, sep='\n')
    return None

find_berry(fruits)