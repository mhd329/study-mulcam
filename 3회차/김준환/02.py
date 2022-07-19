count = 0
strip_lst = []
berry_lst = []

with open('data/fruits.txt','r', encoding='utf-8') as f:
    full_data = f.readlines()
    for berry in full_data:
        strip_lst.append(berry.rstrip())
    for text in strip_lst:
        if text[-5:] == 'berry' and text not in berry_lst:
            print(text)
            berry_lst.append(text)
            count += 1
    print(count)
    #print(berry_lst)

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(str(count)+'\n')
    for berry in berry_lst:
        f.write(berry+'\n')