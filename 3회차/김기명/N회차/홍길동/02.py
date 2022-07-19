b = 0
with open('./data/fruits.txt', 'r', encoding='UTF8') as f:
    t = f.readlines()
    for i in t:
        if 'berry' in i:
            b += 1
with open('02.txt', 'w', encoding='UTF8') as w:
    w.write(i)


    ### 한 문제에 너무심하게 시간을 날려서 일단 보류...