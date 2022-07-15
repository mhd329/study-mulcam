from collections import Counter
from typing import Counter
with open('data/fruits.txt','r',encoding='utf-8')as f:
    count=Counter(f)
    print(f'{count}\n')

'''
- 과일 데이터 `fruits.txt`를 활용하여 과일의 이름과 등장 횟수를  `03.txt` 에 기록하시오.

### 결과 예시

**순서는 달라도 됩니다.**'''