# with open('01.txt', 'w', encoding = 'utf-8') as f:
#     f = open('data/fruits.txt', 'r', encoding = 'utf-8')
#     # print(f.read().count("\n") + 1)
#     print(len(f.readlines()))

with open('data/fruits.txt', 'r') as f:
    fr = f.readlines()
    # print(f.read().count('\n') + 1)

    count = 0
    for i in fr:
        count += 1


with open('01.txt', 'w', encoding = 'utf-8') as fx:
    fx.write(str(count))