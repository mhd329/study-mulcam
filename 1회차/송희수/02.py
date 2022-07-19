with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    names = text.split('\n')
    answer = []
    for name in set(names):
        if name.endswith("berry"):
            answer.append(name)
print(len(answer))
for berry in answer:
    print(berry)

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{len(answer)}\n')
    for berry in answer:
        f.write(f'{berry}\n')
