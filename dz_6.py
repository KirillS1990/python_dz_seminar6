'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''

# Ранее делал задачу также с lambda, сейчас переделал, добавиви фильтр

# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# my_text = del_some_words(my_text)
# print(my_text)


'''
Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]  -> [2, 4, 5, 9]
'''

# переписал программу с list comprehension

# data = [int(value) for value in input('Введите числа последовательно через пробел: ').split()]
# new_data = []
# a = [int(i) for i in data]
# for i in range(len(a)):
#    flag = 1
#    for j in range(len(a)):
#       if a[i] == a[j] and i != j:
#         flag = 0
#         break
#    if flag:
#       new_data.append(a[i])
# print(f'при {data} -> {new_data}')

'''
В файле находится N натуральных чисел, записанных через пробел. 
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
'''

#Задача была на одном из семинаров, переделал с map

# def get_data_from_file(nums):
#     data = open(nums, 'r')
#     dlist = data.read() + ' '
#     dlist = list(map(int, dlist.split()))
#     data.close()
#     return dlist

# def find_number(nums):
#     for i in range(len(nums)-1):
#         if nums[i+1] - nums[i] > 1:
#             return nums[i] + 1


# fnums = 'add_number.txt'
# nums_list = get_data_from_file(fnums)

# print(nums_list)
# print(find_number(nums_list))


# # Добавить недостающее число в список

# def get_full_nums(nums):
#     for i in range(len(nums)-1):
#         if nums[i+1] - nums[i] > 1:
#             nums.insert(i+1, nums[i] + 1)
#     return nums

# nums = get_data_from_file(fnums)

# print(get_full_nums(nums_list))



'''
Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
'''

#переделал задание с использованием enumerate

t_str = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
f = "qwe"
full_list = list(enumerate(t_str))
short_list = list(filter(lambda x: f in x, full_list))
if len(short_list) > 1:
    print(f'список: {t_str}, ищем: "{f}", ответ: {short_list[1][0]}')
else:
    print(f'список: {t_str}, ищем: "{f}", ответ: -1')
