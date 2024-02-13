# import math


# print ('ax^2 + bx + c = 0')

# a = 5
# b = 10
# c = 6

# discr = b*b - 4 * a * c
# #бибилиотека для возведения в степени
# discr =  math.pow (b,2) - 4 * a * c
# print (discr)

# if discr > 0:
#     x1 = (-b+math.sqrt(discr))/(2*a)
#     x2 = (-b-math.sqrt(discr))/(2*a)
#     print ('x1 = ' , x1 , '; x2 = ' , x2)
# elif discr == 0:
#     x = (-b+math.sqrt(discr))/(2*a)
#     print ('x = ' + str(x))
# else :
#     print ('No solutions')


#функции (объединяют общие боки кода)
#объявление функций: def
#название функции: calc_discr
# в скобках пишем аргументы, которые попадают во внутрь функции
import math
def calc_discr (x, y, z):
    print ('a = ' + str(x) + 'b = ' + str(y) + 'c = ' + str (z))
    return math.pow (y,2) - 4 * x * z
def print_result (x, y, z):
    if discr > 0:
        x1 = (-b+math.sqrt(discr))/(2*a)
        x2 = (-b-math.sqrt(discr))/(2*a)
        print ('x1 = ' , x1 , '; x2 = ' , x2)
    elif discr == 0:
        x = (-b+math.sqrt(discr))/(2*a)
        print ('x = ' + str(x))
    else :
        print ('No solutions')
print ('ax^2 + bx + c = 0')

a = 5
b = 10
c = 6

discr = calc_discr (a,b,c)
print (discr)
print_result (x=discr, y=a, z=b)

#допДЗ