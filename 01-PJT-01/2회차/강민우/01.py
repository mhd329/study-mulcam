with open('data/fruits.txt' , 'r' , encoding = 'utf-8') as f :
    lines = f.readlines()
    count = 0
    for a in lines:
        if a in lines:
            count += 1

print(count)

with open('01.txt' , 'w' , encoding = 'utf-8') as f :
    f.write(str(count))
