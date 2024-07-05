with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
  text = f.read().split('\n')
  basket = {}

  for fruit in text:
    if fruit in basket:
      basket[fruit] += 1
    else:
      basket[fruit] = 1

with open('./03.txt', 'w', encoding='utf-8') as f2:
  for key in basket:
    f2.write(key+' ')
    f2.write(str(basket[key])+'\n')