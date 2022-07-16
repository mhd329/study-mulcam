with open("data/fruits.txt", 'r', encoding='utf-8') as f:
    list = f.readlines()

    result = []
    cnt = 0

    for line in list:
        char = line[:-1]
        if char[-5:] == "berry":
            result.append(line)

    num = len(set(result))

with open("02.txt", "w", encoding="utf-8") as ff:
    ff.write(f"{num}\n")
    for i in set(result):
        ff.write(i) 