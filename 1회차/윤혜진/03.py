 # 'fruits.txt' 파일을 한줄씩 읽으면서 과일의 이름과 등장횟수를 딕셔너리 타입의 변수에 기록
with open('1회차/윤혜진/data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = {}
    for fruit in f:
        # fruit 딕셔너리에 해당 과일 key가 없는 경우, 추가
        if fruit.strip() not in fruits:
            fruits[fruit.strip()] = 1
        # fruit 딕셔너리에 해당 과일 key가 있는 경우, 1씩 증가
        else:
            fruits[fruit.strip()] += 1
   

# '03.txt' 파일을 생성한 후, 과일이름과 등장 횟수를 기록
with open('1회차/윤혜진/result/03.txt', 'w', encoding='utf-8') as f:
    for k in fruits:
        f.write(f'{k} {fruits[k]}\n')