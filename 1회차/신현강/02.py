with open('N회차/홍길동/data/fruits.txt', 'r', encoding='utf-8') as f:
    str = []
    for word in f:
        if 'berry' in word:
            str.append(word)
    print(str)
with open('N회차/홍길동/data/fruits.txt', 'r', encoding='utf-8') as f:
    str = ''.join(f)
    print(str.count('berry'))