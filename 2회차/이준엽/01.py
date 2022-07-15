with open('data/fruits.txt', 'r', encoding='utf-8') as f :
    fruit = f.read()
    fruits = fruit.split('\n')
    cnt=0
    for i in fruits :
        cnt+=1
        
    print(cnt)
with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(f'{cnt}')