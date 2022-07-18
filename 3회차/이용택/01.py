with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
  text = f.read().split('\n')
  cnt = len(text)
  
with open('./01.txt', 'w', encoding='utf-8') as f2:
  f2.write(str(cnt))  