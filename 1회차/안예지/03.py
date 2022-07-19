# 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.

with open('data/fruits.txt', 'r', encoding='utf-8') as f :
    text = f.read().split('\n')
    
    fruit_dict = {}
    for word in text :
        
        fruit_dict[word] = fruit_dict.get(word, 0) + 1 
       
    upper = sorted(fruit_dict.items())
    fruit_dict = dict(upper)
with open('03.txt', 'w', encoding='utf-8') as f :
    for name in fruit_dict : 
        sorted(fruit_dict)
        f.write(f'{name} {fruit_dict[name]}\n')
        
    