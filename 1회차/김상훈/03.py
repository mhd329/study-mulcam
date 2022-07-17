with open("data/fruits.txt", "r", encoding="utf-8") as f:
    line = f.readlines()
    dictionary = {}
    for i in line:
        i = i[:-1] #맨뒤 /n 제거
        dictionary[i] = dictionary.get(i, 0) + 1
print(dictionary)
with open("03.txt", "w", encoding="utf-8") as ff:
    for key in dictionary:
        ff.write(f"{key} {dictionary[key]}\n") 
