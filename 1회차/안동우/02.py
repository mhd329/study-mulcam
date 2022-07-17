#- 과일 데이터 `fruits.txt`를 활용하여
#  `berry`로 끝나는 과일의 갯수와 목록을 `02.txt`  에 기록하시오.
#   - 과일은 하나당 한 줄에 기록되어 있습니다.

from hashlib import new
import sys
from types import new_class
from unittest import result

with open('data\\fruits.txt', 'r', encoding= 'utf-8')as a:

     x = a.readlines()

lines = [line.rstrip('\n') for line in x]
#1번문제 여기 까지 동일하다
new_list=[]
for x in lines: 
    if "berry" in x:
       new_list.append(x)
       print(new_list)