import os
with open('00.py','w', encoding='utf-8') as f:
    f.wrtie('N회차 김상훈\n')
    for i in range(1,6):
        f.write(f'{i}일차 파이썬 공부 중\n')