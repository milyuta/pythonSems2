# Урок 6. Ускоренная обработка данных: #lambda, #filter, map, zip, enumerate, #list comprehension. Продолжение
# Посмотреть решенные задачи (семинары и дз 1-6), найти и решить 5 задач с помощью использования лямбд, filter, map, zip, enumerate, list comprehension

# *В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла)





##########################
# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# n = int(input("input the number: "))
# import random 
# my_list = [random.randint(0, 2*n) for i in range(n)]
# print(my_list) 

# sum = 0
# for i in range(1,n,2):
#     sum += my_list[i]
    
# print(f'sum of the uneven elements is : {sum}') 

############### 

# n = int(input("input the number: "))
# import random 
# my_list = [random.randint(0, 2*n) for i in range(n)]
# print(my_list) 

# sum = sum(my_list[i] for i in range(1, len(my_list), 2))
# print(f'sum of the uneven elements is : {sum}')

###############

# 32. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# import random
# n = int(input('Input the number: '))
# my_list = [random.randint(0, n) for i in range(n)]
# print(my_list)

# new_list = []
# [new_list.append(i) for i in my_list if i not in new_list]
# print(f"Your list is: {new_list}")


############## lambda,filter

# import random
# n = int(input('Input the number: '))
# my_list = [random.randint(0, n) for i in range(n)]
# print(my_list)

# new_list = list(filter(lambda p: my_list.count(p) == 1, my_list))

# print(f"Your list is: {new_list}")

#############list comp


# import random
# n = int(input('Input the number: '))
# my_list = [random.randint(0, n) for i in range(n)]
# print(my_list)

# new_list = [p for p in my_list if my_list.count(p) == 1]

# print(f"Your list is: {new_list}")

##################










