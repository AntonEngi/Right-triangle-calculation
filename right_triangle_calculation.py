import math

# рассчёт параметров прямоугольного треугольника
# calculating the parameters of a right triangle
print('\n',"""Для входных данных используется два любых параметра в прямоугольном треугольнике,
углы вводятся последовательно - градусы, минуты, секунды.
В качестве неизвестного проставляется - 0""",'\n')
print("""For input data, any two parameters in a right-angled triangle are used,
angles are entered sequentially - degrees, minutes, seconds.
As an unknown, - 0 is affixed""",'\n')
print("""'Катет а, напротив угла альфа.
Катет b, напротив угла бетта'""")
print("""Leg a, opposite the angle alpha.
Leg b, opposite the angle betta""",'\n')

a = float(input("Enter leg a (Введите катет а)"))
b = float(input('Enter leg b (Введите катет b)'))
c = float(input('Enter the hypotenuse c (Введите гипотенузу с)'))

print("Введите угол альфа противоположный к катету а")
print('Enter angle alpha opposite to leg a')
a_degrees = int(input('degrees (градусы)'))
a_minutes = int(input('minutes (минуты)'))
a_seconds = int(input('seconds (секунды)'))
print("введите угол бетта противоположный к катету b")
print('enter the beta angle opposite to leg b')
b_degrees = int(input('degrees (градусы)'))
b_minutes = int(input('minutes (минуты)'))
b_seconds = int(input('seconds (секунды)'))
print('','\n', '***PARAMETER CALCULATION (РАССЧЁТ ПАРАМЕТРОВ)***')

# перевод градусов в десятичное значение
# convert degrees to decimal
a_decimal = a_degrees + a_minutes / 60.0 + a_seconds / 3600.0
b_decimal = b_degrees + b_minutes / 60.0 + b_seconds / 3600.0

# проверка истинности введённых данных
# checking the truth of the entered data
if a != 0 and b != 0 and c != 0 and c**2 != a**2 + b**2:
    print('Длины сторон треугольника некорректны')
    print('Triangle side lengths are incorrect')
    exit(0)
if a == 0 and b == 0 and c ==0:
    print('One of the sides is needed for accurate rasёt')
    print('Для точного расёта нужна одна из сторон')
    exit(0)
if a != 0 and b != 0 and a_decimal != 0 and math.tan(math.radians(a_decimal)) != a/b:
    print('Некорректные введённые данные')
    print('Incorrect entered data')
    exit(0)
if a != 0 and b != 0 and b_decimal != 0 and 1/math.tan(math.radians(90-b_decimal)) != a/b:
    print('Некорректные введённые данные')
    print('Incorrect entered data')
    exit(0)
if a != 0 and c != 0 and a_decimal != 0 and math.sin(math.radians(a_decimal)) != a/c:
    print('Некорректные введённые данные')
    print('Incorrect entered data')
    exit(0)
if a != 0 and c != 0 and b_decimal != 0 and math.cos(math.radians(b_decimal)) != a/c:
    print('Некорректные введённые данные')
    print('Incorrect entered data')
    exit(0)
if b != 0 and c != 0 and a_decimal != 0 and math.cos(math.radians(a_decimal)) != b/c:
    print('Некорректные введённые данные')
    print('Incorrect entered data')
    exit(0)
if b != 0 and c != 0 and b_decimal != 0 and math.sin(math.radians(b_decimal)) != b/c:
    print('Некорректные введённые данные')
    print('Incorrect entered data')
    
    exit(0)
if a_decimal != 0 and b_decimal != 0 and 90 != a_decimal + b_decimal:
    print('Некорректные введённые данные')
    print('Incorrect entered data')
    print('sum of angles less than 90 degrees')
    exit(0)
if a_minutes >= 60 or a_seconds >= 60 or b_minutes >= 60 or b_seconds >= 60:
    print('Некорректные введённые данные')
    print('Incorrect entered data')
    print('minutes and seconds cannot have a value greater than - 60')
    exit(0)

# рассчёт третьей стороны по двум известным
# third party calculation from two known
if a != 0 and b != 0 and c == 0:
    c = math.sqrt(a ** 2 + b ** 2)
elif a != 0 and b == 0 and c != 0:
    b = math.sqrt(c ** 2 - a ** 2)
elif a == 0 and b != 0 and c != 0:
    a = math.sqrt(c ** 2 - b ** 2)

# перевод углов в радианы
# conversion of angles to radians
rad_alfa = math.radians(a_decimal)
rad_betta = math.radians(b_decimal)

# расчёт противоположного угла при одном из известных (в радианах)
# calculation of the opposite angle with one of the known ones (in radians)
if rad_alfa != 0 and rad_betta == 0:
    rad_betta = math.radians(90) - rad_alfa
if rad_betta != 0 and rad_alfa == 0:
    rad_alfa = math.radians(90) - rad_betta

# расчёт сторон при условии что, известны угол и одна из сторон
# calculation of the sides, provided that the angle and one of the sides are known
if rad_alfa != 0 and c != 0 and a == 0:
    a = c * math.sin(rad_alfa)
    b = c * math.cos(rad_alfa)
if rad_betta != 0 and b != 0 and a == 0:
    c = b / math.cos(rad_alfa)
    a = c * math.sin(rad_alfa)
if rad_betta != 0 and a != 0 and b == 0:
    c = a / math.sin(rad_alfa)
    b = c * math.cos(rad_alfa)
if a == 0 and b == 0 and c == 0:
    print('Нужна хотя бы одна сторона')

# расчёт углов по сторонам
# calculation of angles by sides
if rad_alfa == 0 and rad_betta == 0:
    rad_alfa = math.asin(a / c)

    rad_betta = math.acos(a / c)

a_degrees_pr = math.degrees(rad_alfa)
#a_degrees_pr = round(a_degrees_pr, 40)
b_degrees_pr = math.degrees(rad_betta)
#b_degrees_pr = round(b_degrees_pr, 40)
print('*---***---***---*','\n','')
print("Leg a (Катет a)", a ,'\n'"Leg b (Катет b)", b ,'\n'"Hypotenuse (Гипотенуза)", c)
print('','\n', '--Rounding to 10000s--','\n')
print("Leg a (Катет a)", round(a,4) ,'\n'"Leg b (Катет b)", round(b,4) ,'\n'"Hypotenuse (Гипотенуза)", round(c,4),'\n')
print('Angle alpha in degrees (Угол альфа в градусах)', a_degrees_pr, '\n' "Angle beta in degrees (Угол бетта в градусах)", b_degrees_pr,'\n')
a_dec_deg = math.trunc(a_degrees_pr)
a_dec_min = math.trunc((a_degrees_pr - a_dec_deg) * 60)
a_dec_sec = round((((a_degrees_pr - a_dec_deg) * 60)-a_dec_min)*60)
b_dec_deg = math.trunc(b_degrees_pr)
b_dec_min = math.trunc((b_degrees_pr - b_dec_deg) * 60)
b_dec_sec = round((((b_degrees_pr - b_dec_deg) * 60)-b_dec_min)*60)
print('Angle alpha "deg" ', a_dec_deg,'"min" ',a_dec_min,'"sec" ', a_dec_sec)
print('Angle beta  "deg" ', b_dec_deg,'"min" ',b_dec_min,'"sec" ', b_dec_sec,'\n')
print('Angle alpha in radians', rad_alfa)
print('Angle beta  in radians', rad_betta)
