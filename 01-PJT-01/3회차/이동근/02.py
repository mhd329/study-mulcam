from pprint import pprint

with open("./data/fruits.txt", 'r', encoding="utf-8") as fruits:
    target = "berry\n"

    # 몰랐는데 fruits 파일 내용 중 중복이 있어서 set 을 사용했다.
    data = list(set(filter(lambda x: x.endswith(target), fruits.readlines())))
    data.insert(0, f"{len(data)}\n" )
    pprint(data)

    with open("./data/02.txt", 'w', encoding="utf-8") as output:
        output.writelines(data)