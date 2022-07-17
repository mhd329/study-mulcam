# 이태극님 코드 참고
with open('./data/fruits.txt', 'r',encoding="utf-8") as f:
    #word = input()
    text=f.read()
    fruit=text.split("\n")
    fruit_dict = {}

    for i in fruit:
        if i in fruit_dict:
            fruit_dict[i] += 1
        else:
            fruit_dict[i] = 1
    with open('03.txt', 'w',encoding="utf-8") as a:
        for k,v in fruit_dict.items():
             a.write(str(k)+" ")
             a.write(str(v)+"\n")