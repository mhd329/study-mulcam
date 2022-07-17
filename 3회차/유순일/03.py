# 이태극님 코드 참고
# 딕셔너리 만드는 코드 / 과일이 key이고 숫자가 value.
with open('./data/fruits.txt', 'r',encoding="utf-8") as f:
    #word = input()
    text=f.read()
    fruit=text.split("\n")
    fruit_dict = {}                 # 딕셔너리 코드.

    for i in fruit:
        if i in fruit_dict:
            fruit_dict[i] += 1      # 딕셔너리 안에 문자열을 불러오면서 같은것들은 하나씩 더해.
        else:
            fruit_dict[i] = 1       # 기본값은 1이야.
    with open('03.txt', 'w',encoding="utf-8") as a:
        for k,v in fruit_dict.items():
             a.write(str(k)+" ")
             a.write(str(v)+"\n")