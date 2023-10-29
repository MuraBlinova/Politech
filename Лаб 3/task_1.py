# TODO Напишите функцию для поиска индекса товара
def function_find_item(items_list, item):
    for el in items_list:
        if item == el:
            return items_list.index(el)
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = function_find_item(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
