import sys

with open(r"/Users/mac/Desktop/KDT_PROJ/01-PJT-01/2회차/최준혁/data/fruits.txt", 'r', encoding='utf-8') as f:
    text = f.readlines()
    cnt = 0

    for i in range(len(text)):
        cnt += 1    
    print(cnt)

sys.stdout = open('01.txt', 'w')
print(cnt)
sys.stdout.close()

