with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    count = 0
    linesSet = set(lines) #중복제거
    berryCount = []       
    
for i in linesSet:
    if i.endswith('berry',len(i)-6,len(i)-1):
        count += 1
        berryCount.append(i)
print(count)
for i in berryCount :
    print(i) 


