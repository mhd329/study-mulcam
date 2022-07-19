with open("data/fruits.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    result = {}
    for line in lines:
        line = line[:-1]
        result[line] = result.get(line, 0) + 1

with open("03.txt", "w", encoding="utf-8") as ff:
    for key in result:
        ff.write(f"{key} {result[key]}\n")