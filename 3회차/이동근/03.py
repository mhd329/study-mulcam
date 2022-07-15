from pprint import pprint
from collections import Counter

with open("./data/fruits.txt", 'r', encoding="utf-8") as fruits:
    # 중복 체크하는 것엔collections 모듈 내 Counter 가 가장 먼저 떠올라서 해당 썻다.
    data = dict(Counter(fruits.readlines()))
    
    data = [k.replace('\n', ' ') + str(v) + '\n' for k, v in data.items()]

    with open("./data/03.txt", 'w', encoding="utf-8") as output:
        output.writelines(data)