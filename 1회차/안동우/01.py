import sys

## X는str 출력까지함  count만 하면끝
with open('data\\fruits.txt', 'r', encoding= 'utf-8')as a:
    x = a.read()
    print(type(x))

    