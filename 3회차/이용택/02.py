with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
  text = f.readlines()
  # '\n' 제거 => list
  fruits = []
  for i in range(len(text)):
    fruits += [text[i].strip()]

  # dict type : basket 생성
  # 'berry'로 끝나는 과일 담음
  cnt = 0
  basket = {}
  for fruit in fruits:
    if fruit.endswith('berry'):
      if fruit in basket:
        basket[fruit] += 1
      else:
        basket[fruit] = 1
  # berry_num 구하여 02.txt 작성
  berry_num = len(basket)
with open('02.txt', 'w', encoding='utf-8') as f2:
  f2.write(str(berry_num)) 
