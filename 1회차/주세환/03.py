
with open('data/fruits.txt', 'r', encoding= 'utf-8') as f:
    text = f.read()
    name = text.split('\n')
    result = {}

    for i in name:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
        
print(result)