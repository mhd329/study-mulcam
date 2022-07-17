print("N회차 홍길동")
print("Hello, Python!")
print("1일차 파이썬 공부 중")
print("2일차 파이썬 공부 중")
print("3일차 파이썬 공부 중")
print("4일차 파이썬 공부 중")
print("5일차 파이썬 공부 중")

marks = [75, 76, 77, 78, 79]

number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print("%d일차 파이썬 공부 중" % number)
    else: 
        print("%d일차 파이썬 공부 X." % number)