# 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.


with open('data/fruits.txt', 'r', encoding = 'utf-8') as f: # f란 이름으로 fruits.txt를 읽기 전용으로 열 건데
    text = f.read() # 이 문자열(==text) 안의
    noblank = text.replace(' ', '') # 공백을 지우고(==noblank)
    fruits = noblank.split() # 이걸 리스트로 만들어서(==fruits)
    
    dct = dict() # 이름과 등장횟수 짝을 맞추기 위해 딕셔너리로 만들건데(==dct)
    for fruit in fruits: # fruits 내의 변수들에 대해
        if fruit not in dct.keys(): # 딕셔너리 키 안에 변수가 없다면
            dct[fruit] = 1 # 처음으로 나왔다는 뜻이니까 1을 선언하고
        else: # 그 외엔 중복된다는 뜻이므로
            dct[fruit] += 1 # 값을 추가를 한 다음
    
    for key, value in dct.items(): # 이렇게 나온 dct의 키와 밸류를 동시에 (items 메서드==키와 밸류를 동시에 얻음)
        print(key, value) # 출력함


# output
# Boysenberry 3
# Blueberry 4
# Avocado 1
# Marionberry 3
# Date 9
# Cherimoya 7
# Redcurrant 9
# Longan 4
# Mangosteen 4
# Cloudberry 5
# Loquat 11
# Plumcot 8
# Soursop 1
# Grapefruit 1
# Apricot 3
# Juniperberry 5
# Feijoa 8
# Blackcurrant 4
# Cantaloupe 6
# Salalberry 4
# Fig 4
# Papaya 5
# Elderberry 1
# Yuzu 10
# Quince 2
# Jackfruit 12
# Orange 1
# Uglifruit 4
# Nance 1
# Olive 7
# Cherry 7
# Pomelo 7
# Mulberry 2
# Bloodorange 1
# Plum 2
# Lemon 10
# Coconut 2
# Raspberry 4
# Persimmon 1
# Bilberry 4
# Dragonfruit 3
# Cranberry 4
# Durian 2
# Honeyberry 4
# Pineapple 2
# Watermelon 1
# Rambutan 2
# Plantain 6
# Pear 5
# Gojiberry 2
# Mango 6
# Tamarind 4
# Apple 3
# Solanumquitoense 8
# Starfruit 1
# Banana 2
# Cucumber 15
# Tamarillo 6
# Strawberry 3
# Raisin 3
# Guava 4
# Jambul 4
# Satsuma 3
# Gooseberry 3
# Kumquat 7
# Nectarine 1
# Salak 12
# Prune 3
# Clementine 2
# Lime 4
# Currant 2
# Purplemangosteen 2
# Kiwifruit 1
# Damson 2
# Physalis 2
# Huckleberry 2
# Chicofruit 2
# Salmonberry 3
# Jujube 1
# Custardapple 4
# Passionfruit 2
# Grape 2
# Pomegranate 4
# Lychee 4
# Mandarine 7
# Kiwano 5
# Honeydew 9
# Tangerine 4
# Peach 1
# Jabuticaba 8
# Blackberry 4
# Miraclefruit 9
# Melon 1
# berryfake 1