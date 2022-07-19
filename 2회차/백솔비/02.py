with open('2회차/백솔비/data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    text = list(set(line.rstrip('\n') for line in text))

    answer = []

for name in text:
    if name.endswith("berry"):
        answer.append(name)
print(len(answer))

for berry in answer:
    print(berry)

with open('2회차/백솔비/02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{len(answer)}\n')
    for berry in answer:
        f.write(f'{berry}\n')
