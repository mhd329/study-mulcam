f = open (r'C:\Users\LGE\Desktop\01-PJT-01\1회차\임수경\data\fruits.txt', 'r', encoding = 'utf-8')
    count = 0
    while True:
        if f.readline() == '':
            break
        count += 1
    f.close()

with open ('01.txt', 'w', encoding = 'utf-8') as f:
    f.write(str(count))
    f.close()

    # print('fruits.txt', type('fruits.txt')) #<class 'str'>

    

    
