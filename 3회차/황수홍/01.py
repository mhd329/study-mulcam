with open('./data/fruits.txt', 'r', encoding='utf-8')as f:
    text = f.read()
a = str(text.count('\n')+1)
with open('01.txt', 'w', encoding='utf-8')as f1:
    f1.write(a)