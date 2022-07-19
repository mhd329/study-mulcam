# - 과일 데이터 `fruits.txt`를 활용하여 `berry`로 끝나는 과일의 갯수와 목록을 `02.txt`  에 기록하시오.
#     - 과일은 하나당 한 줄에 기록되어 있습니다.


with open('/Users/senga/Desktop/01-PJT-01/2회차/황지선/data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    list = text.split('\n') # 잘 쪼개진 리스트
    fruit = set(list)
    res = ''
    cnt = 0

    for f in fruit:
        if f.endswith('berry'):
            cnt += 1
            res += f'{f}\n'
    
    with open('02.txt', 'w', encoding='utf-8') as fi:
        fi.write(f'{str(cnt)}\n')
        fi.write(res)