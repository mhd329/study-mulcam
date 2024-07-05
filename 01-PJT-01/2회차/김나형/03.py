with open ("C:/Users/HOME/Desktop/01-PJT-01/2회차/김나형/data/fruits.txt", 'r',encoding='utf-8')as f:
    fruits = f.readlines() 
    fruits = [line.rstrip('\n') for line in fruits]
    new_fruits = {}
    for i in fruits:
        if i in new_fruits:
            new_fruits[i] += 1
        else:
            new_fruits[i] = 1
    print(new_fruits)
    
with open ('03.txt', 'w',encoding='utf-8')as f:
    for key, value in new_fruits.items():
        f.write(f'{key} {value}\n')
