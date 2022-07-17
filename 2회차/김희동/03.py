import pprint
with open('data/fruits.txt', 'r', encoding='utf-8') as f:

    text = f.read()
    fruits = text.split('\n')
    
    cnt = {}

    for abc in fruits:
        if abc in cnt:
            cnt[abc] += 1
        else:
            cnt[abc] = 1

            pprint.pprint(cnt)





with open('03.txt', 'w', encoding='utf-8') as ff:
    for abc in fruits:
        ff.write(f'{cnt}\n')