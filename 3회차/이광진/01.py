# 01. 텍스트 데이터 입력 (연습)
# 과일 데이터 `fruits.txt`를 활용하여 총 과일의 갯수를 `01.txt`  에 기록하시오
# output : 394

# with open('data/fruits.txt', 'r', encoding = 'utf-8'):
#     print('hi')
#     a = 'hihihi'

# with open('a.txt', 'w', encoding = 'utf-8') as f:
#     f.write(a)

with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    fruit = f.read()
    print(fruit)
    
    
    
    
    # for line in f:
    #     print(line, end='')

    # lines = f.readline()
    # print(lines)
    


# with open('students.txt', 'r', encoding='utf=8') as f:
#     # 텍스트는 string 타입
#     text = f.read()
#     print(text, type(text))
#     # string.split() => list 타입
#     names = text.split()
#     cnt = 0
#     for name in names:
#         # name : 첫 번째 시행 - 가민지
#         # 언제? 마씨?
#         if name.startswith('마'):
#         # if name[0] == '마':
#             cnt += 1
#     print(cnt)