with open('N회차/홍길동/data/fruits.txt', 'r', encoding='utf-8') as f:

    # char_count = {}
    # for letter in f:
    #     if not (letter in char_count):
    #         char_count[letter] = 1
    #     else:
    #         char_count[letter] += 1

    char_count = {}
    for letter in f:
        print("%c = %d" % (letter, char_count[letter]))

