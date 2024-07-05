count = 0

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    for line in f:
        count += 1

with open('01.txt', 'w', encoding='utf-8') as txt_01:
    txt_01.write(str(count))
    txt_01.close()