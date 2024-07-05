fruit = open("data/fruits.txt","r",encoding="UTF-8")
count=0
for i in fruit:
    count = count + 1 
print(count)