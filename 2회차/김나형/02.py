# with open("C:/Users/HOME/Desktop/01-PJT-01/2회차/김나형/data/fruits.txt", 'r', encoding='utf-8')as f:
#     fruits = f.read().split()


# new_fruits = set(fruits)
# cnt = 0
# result = ""
# for i in new_fruits:
#     if i[-5:] == 'berry':
#         cnt += 1
# print(cnt)

# for i in new_fruits:
#     if i[-5:] == 'be->ㅖrry':        
#         print(result)
#         result = result + i +'\n'

    
# with open('02.txt', 'w', encoding='utf-8')as f:
#     f.write(f'{cnt}\n')
#     f.write(f'{result}')


with open('data/fruits.txt', 'r', encoding='utf-8')as p: # f : 별명
    new_fruits = p.readlines() 
    new_fruits = [line.rstrip('\n') for line in new_fruits]
    result = []
    for i in new_fruits:
        
        if i.endswith('berry'):
            if not i in result:
                result.append(i)
    # print(len(result))
    # for x in result:
    #     print(x)

with open('02.txt', 'w', encoding='utf-8')as f:
     f.write(f'{len(result)}\n')
     for x in result:
        f.write(f'{x}\n')
