#- 내용을  `00.txt`에 기록하시오.

# 00.txt 파일 open
#해당 글 작성

with open('00.txt','w',encoding = 'utf-8') as f:
    f.write('3회차 최태진\n')
    f.write('Hello, Python!\n')
    for char in range(1,6):
        f.write(f'{char}일자 파이썬 공부 중\n')
    
with open('00.txt','r',encoding = 'utf-8') as f:
    print(f.read())
