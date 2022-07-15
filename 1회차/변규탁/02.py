
with open('./data/fruits.txt', 'r', encoding='utf-8') as file:
    
    lines = file.readlines()
    A = set()
    
    for line in lines:
        if line.endswith('berry\n'):
            A.add(line)
    

with open('02.txt', 'w', encoding='utf-8') as file:
    file.write(str(len(A)))
    file.write('\n')
    file.writelines(A)