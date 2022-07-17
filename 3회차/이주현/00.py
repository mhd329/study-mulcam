

# 유니코드-8 방식, 파일로서 00.txt라는 파일이름을 쓰기방식으로 연다
with open('00.txt','w', encoding='utf-8') as f:
    f.write("3회차 이주현\n")
    f.write("Hello, python!\n")
    for i in range(1,6):
        f.write(f'{i}일차 파이썬  공부 중\n')



