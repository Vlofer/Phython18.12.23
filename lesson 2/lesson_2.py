import math
import time

if __name__ == '__main__':
    t0 = time.time()
    # int - integer
    # целое число
    x1 = 15
    x2 = 7
    print(x1)
    print(type(x1))
    print(type(x1) == int)

    print(x1 + x2)
    print(x1 * x2)
    print(x1 - x2)
    print(f'Dilenie:', x1 / x2)
    print(type(x1 / x2))
    print(f'two palocka', x1 // x2)
    print(f'{x1} % {x2} =', x1 % x2)
    print(type(x1 // x2))
    print(f'{x1} * {x2} =', x1 ** 2)
    print(pow(x1, 1/2))
    print(x1 * (1/2))

    print(f'Divmod{divmod(x1, x2)}')

    # float - плавающее число
    # floating point
    print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFLOOOOOOOOOOOOOOOOOOOOAAAAAAAAAAAAAAATTTTTTTTTTT")
    y1 = 2.54931321
    y2 = 6.13
    print(y1)
    print(int(y1))
    print(f'Round 2: {round(y1, 2)}')
    #ceil - потолок

    print(f'Ceil {math.ceil(y1)} type {type(math.ceil(y1))}' )

    #floor - пол

    print(f'floor {math.floor(y1)} type{type(math.floor(y1))}')
    print(type(y1))
    #Вычитания
    print(f'Subtract: {y1 - y2} absolute value: {abs(y1 - y2)}')
    print(f'Negative power of 5: {-5 ** 2} {-5 ** 3} {-5 ** 999}')

    #time.sleep(5.05)
    print(f'Наша программа выполняется за: {round(time.time() - t0, 1)}')

    #str - string - строка
    print('I line in Ukraine' .encode('utf-8'))

    s = "i line in Ukraine"
    print(s.lower())
    print(s.upper())
    p =  'python'
    print(p.title())
    print(s.upper(), s.upper().title())
    print(s.upper().capitalize(), s.capitalize())
    s = '''
I live in Ukraine
I code on Python
My name in Vlad'''
    print(s)
    print(s.title())
    print(s.capitalize())
    print(s.upper())
    print(s.lower())

    print(s)
    s = 'Python'
    print('is digit', s, s.isdigit())
    s = '5.0'
    print('is digit', s, s.isdigit())
    print('is numeric', s, s.isnumeric())
    print('is decimal', s, s.isdecimal())
    print('Python__'.strip('_'))
    x = input('Введите число: х=')
    print(x.lstrip('-').isdigit())
    try:
        int(x)
    except Exception:
        print('Это не число')

s = 'I am from Ukraine'
s = s.replace("Ukraine", "Fastiv")
print(s)
print(s.find('Fastiv'))




