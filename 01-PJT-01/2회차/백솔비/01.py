with open('2회차/백솔비/data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits_len = str((len(f.readlines())))

with open('2회차/백솔비/01.txt', 'w', encoding='utf-8') as f:
    f.write(fruits_len)
