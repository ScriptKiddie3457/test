# X = 0
# try:
#     print('start code')
#     print(10 / X)
#     print('no errors')
# # except NameError as ex:
# #     print(f'we have an error: {ex}')
# # except ZeroDivisionError as ex:
# #     print(f'we have an error: {ex}')
# except (NameError, ZeroDivisionError) as ex:
#     print(f'we have an error: {ex}')
#
# try:
#     try:
#         print('start code')
#         print(10 / x)
#         print('no errors')
#     except NameError as ex:
#         print(ex)
# except (NameError, ZeroDivisionError) as ex:
#     print(f'we have an error: {ex}')
# print('code after')
#
# try:
#     print('start code')
#     print(10 / 0)
#     print('no errors')
# except (NameError, ZeroDivisionError) as ex:
#     # працює коли є помилка
#     print(f'we have an error: {ex}')
# else:
#     # працює коли нема помилки
#     print("no errors")
# finally:
#     # працює незалежно від помилки
#     print('finally code')


# def checker(value):
#     if not isinstance(value, str):
#         raise TypeError(f'sorry we cant work with {type(value)}. We need only str')
#     else:
#         return 'Niceeee' + value
# checker(100)

# class BuildingError(Exception):
#     def __init__(self, amount, limit):
#         self.amount = amount
#         self.limit = limit
#
#     def __str__(self):
#         return (f'Not enough materials to build!',
#                 f'we need at least {self.limit}, but got {self.amount}')
#
#
# def check_materials(amount, limit):
#     if amount >= limit:
#         print('yes we can build the house!')
#     else:
#         raise BuildingError(amount, limit)
#
#
# check_materials(100, 250)


import warnings

# warnings.simplefilter('always', ImportWarning)
# # warnings.simplefilter('always', SyntaxWarning)
# warnings.simplefilter('ignore', SyntaxWarning)
#
# warnings.warn('warning, no code here', SyntaxWarning)
# warnings.warn('warning, wrong import', ImportWarning)
# print("Hello World")

warnings.simplefilter('error', ImportWarning)
try:
    warnings.warn('warning, wrong import', ImportWarning)
except:
    print('Warning processed')
