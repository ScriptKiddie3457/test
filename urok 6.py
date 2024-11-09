X = 0
try:
    print('start code')
    print(10 / X)
    print('no errors')
# except NameError as ex:
#     print(f'we have an error: {ex}')
# except ZeroDivisionError as ex:
#     print(f'we have an error: {ex}')
except (NameError, ZeroDivisionError) as ex:
    print(f'we have an error: {ex}')

try:
    try:
        print('start code')
        print(10 / x)
        print('no errors')
    except NameError as ex:
        print(ex)
except (NameError, ZeroDivisionError) as ex:
    print(f'we have an error: {ex}')
print('code after')

try:
    print('start code')
    print(10 / 0)
    print('no errors')
except (NameError, ZeroDivisionError) as ex
    # працює коли є помилка
    print(f'we have an error: {ex}')
else:
    # працює коли нема помилки
    print("i am else")
finally:
    # працює незалежно від помилки
    print('finally code')