with open("data/fruits.txt", "r", encoding="utf-8") as f:
    line = f.readlines()
<<<<<<< HEAD
    dic = {}
    for i in line:
        i = i[:-1]
        dic[i] = dic.get(i, 0) + 1
        
with open("03.txt", "w", encoding="utf-8") as ff:
    for key in dic:
        ff.write(f"{key} {dic[key]}\n") 
=======
    print(line)
    dictionary = {}
    for i in line:
        i = i[:-1] #맨뒤 /n 제거
        dictionary[i] = dictionary.get(i, 0) + 1
print(dictionary)
with open("03.txt", "w", encoding="utf-8") as ff:
    for key in dictionary:
        ff.write(f"{key} {dictionary[key]}\n") 
>>>>>>> 6cb3752de837207a52ee476bb4a4abebc19c0b6f
