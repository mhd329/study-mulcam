with open("data/fruits.txt", 'r', encoding='utf-8') as f:
    fruit = list(f.read().split('\n'))
    
berry = []
for i in fruit:
    if i[-1] == "y" and i[-2] == 'r' and i[-3] == 'r' and i[-4] == 'e' and i[-5] =='b':
        berry.append(i)

berries = []
for i in berry:
    if i in berries:
        continue
    else:
        berries.append(i)
        
print(len(berries))
for i in berries:
    print(i)