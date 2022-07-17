import sys

with open('data\\fruits.txt', 'r', encoding= 'utf-8')as a:
    # 텍스트파일 인코딩하고
    x = a.readlines()
    #readlines(리스트변경)
lines = [line.rstrip('\n') for line in x]
# rstrip 인자 제거 인자가 없을 경우 오른쪽 공백제거  
f= open('01.txt', 'w')
f.write(str(len(lines)))
#write는 인자가 str이어야합니다
f.close()
#394