# f에 data폴더 fruits 텍스트파일을 읽기방식으로 넣어준다.
f = open('./data/fruits.txt', 'r', encoding='UTF8')

# lines에 한줄씩 넣어준다.
lines = f.readlines()

# 리스트의 길이를 count에 넣어준다.
count = len(lines)

print(count)
