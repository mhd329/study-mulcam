with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.read().split('\n')

# b = 'berry'
# list = []
# result = []
# cnt = 0

# for i in fruits:
#     if b in i:                  # berry가 i 에 존재할때
#         list = i.split('\n')    # 모든 berry가 리스트로 출력
#         # print(list, type(list))
#     for berry in list:
#         if berry not in result:
#             result.append(berry)
#             cnt += 1

# print(result)
# # berryfake까지 리스트 출력....

cnt = 0
berry_list = []
final_list = []

for i in fruits:
    if i.endswith('berry'):
        berry_list.append(i)            # berry로 끝나는 단어를 리스트로 반환
    for result in berry_list:           # berry_list에 있는 단어를 하나씩 꺼냄
        if result not in final_list:    # final_list에 result와 똑같은 값이 없으면,
            cnt += 1
            final_list.append(i)        # final_list에 단어를 넣는다

list = '\n'.join(final_list)

print(cnt)
print(list)

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{cnt}\n{list}')