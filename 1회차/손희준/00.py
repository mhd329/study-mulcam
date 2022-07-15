import sys
sys.stdout = open('00.txt','w',encoding= 'utf-8')

text1 = "N회차 홍길동\nHello, Python!"
print(text1)
n = 5
for i in range(n):
    print(i+1,"일차 파이썬 공부 중")
