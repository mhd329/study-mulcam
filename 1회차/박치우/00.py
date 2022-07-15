with open('1회차/박치우/00.txt','w',encoding='utf-8')as f:
    f.write('1회차 박치우')
    f.write('Hello, Python!')
    for i in range(5):
        print('{0}일차 파이썬 공부 중'.format(i))
