# - 과일 데이터 `fruits.txt`를 활용하여 `berry`로 끝나는 과일의 갯수와 목록을 `02.txt`  에 기록하시오.
#     - 과일은 하나당 한 줄에 기록되어 있습니다.

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

    result = []
    cnt = 0

    for line in lines:
        char = line[:-1]
        if char[-5:] == "berry":
            result.append(line)

    print(len(set(result)))
 
with open('02.txt','w', encoding="utf-8") as f:
    f.write(f"{len(set(result))}\n")
    for i in set(result):
        f.write(i)    