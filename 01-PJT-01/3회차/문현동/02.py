cnt = 0
berries = []
res = []

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    
    fruits = f.read()
    fruits_list = fruits.split("\n")
    for something in fruits_list:
        if something.endswith("berry"):
            berries.append(something)

    berry = list(set(berries))
    
    for someberry in berry:
        cnt += 1
        res.append(someberry)

with open('02.txt', 'w', encoding='utf-8') as br:
    br.write(f'{cnt}\n')
    for i in res:
        br.write(f'{i}\n')