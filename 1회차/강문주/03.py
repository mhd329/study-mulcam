with open('data/fruits.txt','r',encoding='utf-8') as f:
    num=0
    for i in f:
        print(i)
            # if i in f:
        #     f[i]+=1
            
        
        # print(i, num, end='')

'''from collections import Counter
from pprint import pprint
from typing import Counter
with open('data/fruits.txt','r',encoding='utf-8')as f:
    count=Counter(f)
    pprint(f'{count}')
'''
'''
- 과일 데이터 `fruits.txt`를 활용하여 과일의 이름과 등장 횟수를  `03.txt` 에 기록하시오.

### 결과 예시

**순서는 달라도 됩니다.**'''