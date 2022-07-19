import sys
with open(r"/Users/mac/Desktop/KDT_PROJ/01-PJT-01/2회차/최준혁/data/fruits.txt", 'r', encoding='utf-8') as f:
    text = f.readlines()
    lines = list(set(text))
    cnt = 0
    end_berry = []
    for name in lines:
        if 'berry' in name:
            cnt += 1
            if name.startswith('berry'):
                cnt -= 1
                continue
            end_berry.append(name)
            print(name)
    print(cnt)

sys.stdout = open('02.txt', 'w')
for i in range(0, 18):
    print(end_berry[i])
print(cnt)
sys.stdout.close()

