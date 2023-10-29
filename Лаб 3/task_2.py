# TODO Напишите функцию find_common_participants

def sort_key(str_):
    return str_[0]

def find_common_participants(str_a, str_b, separator=','):
    list_a = str_a.split(separator)
    list_b = str_b.split(separator)
    ans = list(set(list_a).intersection(list_b))
    ans.sort()
    return ans


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, separator='|'))