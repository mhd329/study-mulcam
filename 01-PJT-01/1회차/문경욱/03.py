from cgi import print_arguments


fruit_dict = {}
fruit_list = []
fruit_chr = ""
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    # 딕셔너리에 과일이름/등장 횟수 저장
    for name in f:
        name = name.rstrip('\n')
        if not name in fruit_dict:
            fruit_dict[name] = 1
        else:
            fruit_dict[name] += 1

with open('03.txt', 'w', encoding='utf-8') as f:
    for key in fruit_dict:
        f.write(f'{key} : {fruit_dict[key]}\n')