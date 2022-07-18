with open('./00.txt', 'w', encoding='utf-8') as f:
  f.write('3회차 이용택\n')
  f.write('Hello, Python!\n')
  for i in range(1,6):
    if i == 5:
      f.write(f'{i}일차 파이썬 공부 중')
    else:
      f.write(f'{i}일차 파이썬 공부 중\n')