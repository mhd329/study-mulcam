with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
  text = set(f.read().split('\n'))
  cnt = 0
  basket = []

  for fruit in text:
    if fruit.endswith('berry'):
      basket += [fruit]
      cnt += 1

with open('./02.txt', 'w', encoding='utf-8') as f2:
  f2.write(str(cnt)+'\n')
  for word in basket:
    f2.write(word+'\n')