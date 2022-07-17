with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = text.split()
    fruits_set = set(fruits)
    fruits = list(set(fruits_set))
    
    with open('02.txt', 'w', encoding='utf-8') as w:
        count = 0
        
        for fr in fruits:
            if fr.endswith('berry'):
                count += 1        
        
        w.write(f'{count}\n')
        
        for fr in fruits:
            if fr.endswith('berry'):
                count += 1
                w.write(f'{fr}\n')

