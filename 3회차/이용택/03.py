with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
  fruits = f.readlines()
  for i in range(len(fruits)):
    fruits[i] = fruits[i].strip()
  
  basket = {}
  for fruit in fruits:
    if fruit in basket:
      basket[fruit] += 1
    else:
      basket[fruit] = 1
  
with open('03.txt', 'w', encoding='utf-8') as f2:
  for key in basket:
    f2.write(str(key))
    f2.write(str(basket[key])+'\n')