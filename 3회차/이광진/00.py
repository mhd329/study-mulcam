## 00. 텍스트 데이터 출력 (연습)

# - 아래의 내용을  `00.txt`에 기록하시오.

with open('data/00.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text, type(text))