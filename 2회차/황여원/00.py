with open('00.txt', 'w', encoding="utf-8") as f:
    
    f.write('2회차 황여원\n')
    f.write('Hello Python\n')

    for i in range(5):
        f.write(f"{i+1}일차 파이썬 공부중\n") 

# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write('Happy Hacking!\n')
#     for i in range(1, 6):
#         f.write(f'{i} 번째!\n')