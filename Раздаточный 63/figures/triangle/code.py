import math

def triangle_perimeter(a = 7, b =2, c = 8):

    perimeter = int(a) + int(b) +int(c)
    print('Периметр треугольника', perimeter)




def triangle_area(a = 7, b =2, c = 8):

    p = (int(a) + int(b) + int(c)) * 0.5
    res = p*((p-a)*(p-b)*(p-c))
    area = math.sqrt(res)
    print('Площадь треугольника', area)

