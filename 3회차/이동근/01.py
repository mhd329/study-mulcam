with open("./data/fruits.txt", 'r', encoding="utf-8") as fruits:
    with open("./data/01.txt", 'w', encoding="utf-8") as output:
        output.writelines(fruits.readlines())
        
    # readlines, writelines document
    # https://docs.python.org/3/library/io.html?highlight=readlines#io.IOBase.readlines
    # https://docs.python.org/3/library/io.html?highlight=writelines