my_data = int(input("Введите количество наименований товаров, для внесения в базу: "))
n = 1
my_info = {}
my_base = []
product_analytics = ()
while n <= my_data:
    my_info = dict({'название': input("введите название: "), 'цена, руб': input("Введите цену: "),
                    'количество, шт': input('Введите количество: '), 'гарантия, лет': input("Введите срок гарантии: ")})
    my_base.append((n, my_info))
    n += 1
sum_info = tuple(my_base)
product_analytics = (
        {'название': my_info.get('название'), 'цена, руб': my_info.get('цена, руб'), 'количество, шт': my_info.get('количество, шт'),
         'гарантия, лет': my_info.get('гарантия, лет')})

