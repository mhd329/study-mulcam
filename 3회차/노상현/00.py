# 아래의 내용을  00.txt에 기록하시오.

with open('00.txt', 'w', encoding='UTF-8') as f:

    f.write('N회차 노상현\n')
    f.write('Hellom, Python!\n')
    
    for i in range(1,6):
    
        f.write(f'{i}일차 파이썬 공부 중\n')
