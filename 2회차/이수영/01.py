with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
count = 0
fruits = text.split('/n') # 'apple'  'mango' => 'apple mango' 
for i in fruits:
    count += 1
print(fruits)


with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(count))