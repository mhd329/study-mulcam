with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
n = 0
fruits = text.split('\n')
result =[]
for chr in fruits:
    if chr[-5:] == 'berry':
        result.append(chr)

berry = set(result)  # set으로 중복 제거

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{str(len(berry))}\n')
    for i in berry:
        f.write(f'{i}\n')  
   
        
        

    

            

