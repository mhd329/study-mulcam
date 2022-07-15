with open ('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    frt = text.split('\n')
    berrys = []

    for f in frt:
        if f[-5:] == 'berry':
            berrys.append(f)    
    print(set(berrys), len(set(berrys)))
    n = len(set(berrys))

with open ('02.txt', 'w', encoding='utf-8') as f:
    f.write(str(set(berrys)))
    f.write(str(n))