# cem = 0
# def show():
#     global cem
#     cem += 1                                                  ### FUNKSIYANIN NETICESI:1
#     print('funksiyanin neticesi:', cem)           ###NETICE 
#                                                               ### GLOBAL CEM:1
# show()
# print('global cem:', cem)

# cem = 0
# def show():
#     global cem
#     cem += 1                                                  ### FUNKSIYANIN NETICESI:1
#     print('funksiyanin neticesi:', cem)           ###NETICE 
                                                                ### GLOBAL CEM:0
# print('global cem:', cem)                        
# show()                                                         
# print('global cem:', cem)                                     ### GLOBAL CEM:1       

# def main():
#     global x
#     x = 5
#     print(x)

# main()
# print(x)

# ##DECORATORS IN PYTHON
# ##  PARAMETR-ARQUMENT
# def my_func(func):
#     def decorate():
#         print('Salam necesen?')
#         func()
#         print('Mende yaxsiyam')
#     return decorate()
# def main():
#     print('Yaxsiyam sen necesen?')
# my_func(main)

# def my_func(func):
#     print('Salam necesen?')
#     func()
#     print('Mende yaxsiyam')   
# def main():
#     print('Yaxsiyam sen necesen?')
# my_func(main)

# def my_func(func):
#     def decorate():
#         print('Start')
#         func()
#         print('Stop')
#     return decorate

# @my_func
# def main():
#     print('XX')
# main()

# def main():
#     print('Hello')
#     main()
# main()

# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
# for i in range(1,15):
#     print((i), ':' , fibonacci(i))

# my_list = [1,2,3,4,5,6,7,8,9]
# c = []

# for i in my_list:
#     if i % 2 == 0:
#        c.append(i)
# print(c)

# new_list = [i for i in range(21)]
# print(new_list)

# my_list = [1,2,3,4,5,6,7,8,9]
# new_list = [i for i in my_list if i % 2 == 0]
# print(new_list)

# try:
#     a = 5
#     print(a/0)
# except ValueError:
#     print('not found')
# except ZeroDivisionError:
#     print('0-a bolme olmaz')
# finally:
#     print('Finall')