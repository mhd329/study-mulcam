fruit = open("data/fruits.txt", "r", encoding="UTF-8")
new_list = []

cnt = 0
for i in fruit:
    i = i.rstrip('\n')
    if i[-5:] == 'berry':
        if i not in new_list:
            new_list.append(i)
            print(i)
            cnt += 1

print(cnt)