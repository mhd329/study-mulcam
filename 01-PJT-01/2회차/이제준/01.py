with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.read()
    list = fruits.split('\n')       
# .split() 을 통해 리스트를 만든다. 
# 하지만, '\n'이 없으면, Salal berry도 두개의 리스트로 나뉘어진다.
# 즉 \n 를 써서, 새로운 줄일때마다 리스트를 만드는 것으로 설정한다
# 과일은 하나당 한줄!!!

cnt = 0
for i in list:
    cnt += 1
print(cnt)

with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(f'{cnt}')