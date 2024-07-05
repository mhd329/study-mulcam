
f = open('./data/fruits.txt', 'r', encoding = 'utf-8')

ff = f.read()
ff = ff.split('\n')
cnt = 0
ff = set(ff)
for i in ff :
    if 'berry' in i and i[-1] == 'y' :
        cnt += 1
        print(i)
print(cnt)