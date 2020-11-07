# task1
# def all_num(num):
#     '''эта функция возвращает числа от 1 до заданного'''
#     if num == 1:
#         return 1
#     else:
#         return str(all_num(num - 1)) + " " + str(num)
# print(all_num(int(input("введите число: "))))

# task2
# def some_rec(num):
#     '''эта функция возвращает сумму чисел от 1 до данного числа'''
#     if num == 0:
#         return num
    
#     return num + some_rec(num - 1)   
# print(some_rec(int(input("введите число: "))))

# task3
# def reverse_num(num, null):
#     '''эта функция возвращает обратную запись числа'''
#     if num == 0:
#         return null
#     else:
#         return reverse_num(num//10, null*10 + num%10)
# n = int(input("введите число: "))
# zero = 0
# print(reverse_num(n, zero))

# task4
# def fib_rec(num):
#     '''эта функция возвращает число Фибоначи'''
#     if num <= 1:
#         return num

#     return fib_rec(num - 1) + fib_rec(num - 2)

# print(fib_rec(int(input("введите число: "))))

# task5
# def stepPerms(n):
#     '''эта функция возвращает количество разрадов шагов'''
#     if n == 1 or n == 0:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return stepPerms(n - 3) + stepPerms(n - 2) + stepPerms(n - 1)
# print(stepPerms(int(input("введите шаг: "))))