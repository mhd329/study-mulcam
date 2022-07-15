with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
  text = f.readlines()
  fruits = []
  for i in text:
    fruits += [i.strip()]
    fruits_cnt = len(fruits)
with open('01.txt', 'w', encoding='utf-8') as f2:
  f2.write(str(fruits_cnt))


  