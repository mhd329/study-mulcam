fruit_list = []

with open('data\\fruits.txt', 'r') as f:
    lines = f.readlines()
    fruit_list = list(map(lambda s: s.strip(), lines))

fruit_berry = [fruit for fruit in fruit_list if fruit.endswith('berry')]
fruit_berry = set(list(fruit_berry))

with open('02.txt', 'w') as f1:
    f1.write(str(len(fruit_berry))+'\n')
    for fruit in fruit_berry:
        f1.write(fruit+'\n')
