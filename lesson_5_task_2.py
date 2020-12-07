with open('file_2.txt', 'r') as my_obj:
    content = my_obj.readlines()
    print(content)
    print(f'количество строк {len(content)}')
    for x, i in enumerate(content):
        words = len(i.split())
        print(f' Число слов в строке {x + 1} - {words} \n')
