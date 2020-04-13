import string

text_from_file = open('text.txt','r',encoding='UTF8')
text_to_program = text_from_file.read()
text_from_file.close()
print(text_to_program)

# 1) методами строк очистить текст от знаков препинания

# list_marks = []
list_marks = ['.',',',';',':','«','»','—','!','?']
text_without_marks = text_to_program

for item in list_marks:
    text_without_marks = text_without_marks.replace(item,'')

print(text_without_marks)

# 2) сформировать list со словами (split)

list_split = text_without_marks.split()
print(list_split)

# 3) привести все слова к нижнему регистру (map);

lower_list = list(map(lambda x:x.lower(),list_split))
print(lower_list)

# 3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте

set_from_list = set(lower_list)
dict_from_list = {}

for element in set_from_list:
    dict_from_list[element] = lower_list.count(element)

print(dict_from_list)

# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set)

list_items = list(dict_from_list.items())
list_items.sort(key=lambda i:i[1],reverse=True)
# Вариант 1
set_list_items = set(list_items[:5])
print(set_list_items)
# Вариант 2
print(list_items[:5])

# 5) выполнить list с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

lim_list_split = list(map(lambda word: morph.parse(word)[0].normal_form, lower_list))
print(lim_list_split)
# удаляем повторяющиеся слова
lim_list_split = list(dict.fromkeys(lim_list_split))
print(lim_list_split)