with open('00.txt', 'w', encoding='utf-8') as f:
  name = '이용택'
  class_num = 3
  msg = 'Hello, Python!'
  f.write(f'{class_num}회차 {name}\n')
  f.write(msg+'\n')
  for i in range(1,6):
    if i == 5:
      f.write(f'{i}일차 파이썬 공부 중')
      break
    f.write(f'{i}일차 파이썬 공부 중\n')
