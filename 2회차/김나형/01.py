with open("C:/Users/HOME/Desktop/01-PJT-01/2회차/김나형/data/fruits.txt", 'r', encoding='utf-8')as f:
    fruits = f.read().split()
    s = len(fruits)
    print(s)
with open('01.txt', 'w', encoding='utf-8')as f:
    f.write(f'{s}')
