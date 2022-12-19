# '''3'''

# # class KgToPounds:
    
# #     __kg = 0
    
# #     def to_pounds(self):
# #         return self.__kg * 2.2
# #     def set_kg(self, new_kg):
# #         self.__kg = new_kg
# #     def get_kg(self):
# #         return self.__kg


# # evgeniy = KgToPounds()

# # evgeniy.set_kg(float(input('KG = ')))
# # print(evgeniy.to_pounds())

# # ----------------------------------------------------------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------------------------------------------
# '''4'''
# # Николай – оригинальный человек. 
# # Он решил создать класс Nikola, принимающий при инициализации 2 параметра: 
# # имя и возраст. Но на этом он не успокоился. 
# # Не важно, какое имя передаст пользователь при создании экземпляра, оно 
# # всегда будет содержать “Николая”. 
# # В частности - если пользователя на самом деле зовут Николаем, то с именем 
# # ничего не произойдет, а если его зовут, например, Максим, то оно 
# # преобразуется в “Я не Максим, а Николай”.
# # Более того, никаких других атрибутов и методов у экземпляра не может быть 
# # добавлено, даже если кто-то и вздумает так поступить (т.е. если некий 
# # пользователь решит прибавить к экземпляру свойство «отчество» или метод 
# # «приветствие», то ничего у такого хитреца не получится).


# class Nikola:
#     def __init__(self, __name, __age) -> None:
#         self.__name = __name
#         self.__age = __age

#     def set_name(self, new_name):
#         self.__name = new_name
#     def set_age(self, new_age):
#         self.__age = new_age
#     def get_name(self,__name):
#         return self.__name
#     def get_age(self,__age):
#         return self.__age
# name = str(input('Name:   '))
# age = int(input('Age:    '))        
# nikolay = Nikola(name,age)
# # nikolay.set_age()

# if name != 'Nikolay':
#     nikolay.set_name('Nikolay')

# print(f'{nikolay.get_name(name)} is {nikolay.get_age(age)} years old')

# return new_func()

# class Triangle:
    
#     def __init__(self, a : float, b : float, c : float) -> None:
#         self.a = a
#         self.b = b
#         self.c = c
#     def is_triangle(self):
#         if isinstance(self.a, float) and isinstance(self.b, float) and isinstance(self.c, float):
#             if self.a > 0 and self.b > 0 and self.c > 0:
                
#                 if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
#                     return 'GOOD'
#                 else:
#                     return 'No Triangle'
#             else:
#                 return 'Wrong input'
#         else:
#             return 'Wrong input'
        
# try:
#     x = Triangle(float(input('a = ')), float(input('b = ')), float(input('c = ')))
#     print(x.is_triangle())
# except ValueError:
#     print('Wrong Input')
    
# -----------------------------------------------------------------------------------------------------------------
    
'''Problem 1'''

 
# from typing import Callable, Any
# import functools


# def Vasya(how_are_you : Callable) -> Any:
#     functools.wraps(wrapped='how_are_you')
#     def vasya_decorator(*args):
#         print('Я не очень, вот твоя функция')
#         how_are_you(*args)
#     return vasya_decorator
# @Vasya
# def some_func(answer):
#     print('Функция работает ...')

# some_func(input('How are you -- '))

    
# -----------------------------------------------------------------------------------------------------------------

'''Problem 2'''

# # Delay before completing the function

# from typing import Callable, Any
# import functools
# import time

# def timer_delay(delay: Callable) -> Any:
    
#     @functools.wraps(wrapped=delay)
#     def delay_decorator():
#         '''Documentation'''
        
#         print('Loading...')
#         time.sleep(0.5)
#         delay()
#     return delay_decorator

# @timer_delay
# def some_func():
#     '''Documentation'''
#     print('Function is complete')
    
# some_func()
# print(some_func.__name__)
# print(some_func.__doc__)

# -----------------------------------------------------------------------------------------------------------------




