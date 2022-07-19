with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    names = text.split('\n')
    numbers_counter = {}
    for fruits in names:
        if fruits not in numbers_counter:
            numbers_counter[fruits] = 1
        
        else:
            numbers_counter[fruits] += 1
    
    for key, value in numbers_counter.items():
        print(key, value)

with open('03.txt', 'w', encoding='utf-8') as f:
    for key, value in numbers_counter.items():    
        f.write(f'{key} {value}\n')