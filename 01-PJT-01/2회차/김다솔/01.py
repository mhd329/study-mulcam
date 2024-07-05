with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    l = f.readlines()
    count = 0
    for list in l:
        count += 1
        result = str(count)
              
with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(result)     