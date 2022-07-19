fruit = open("data/fruits.txt", "r", encoding="UTF-8")
cnt = 0
for i in fruit:
    i = i.rstrip('\n')
    print(i,type(i))
    if i[-6:] == 'berry':
        print(i)

print(cnt)