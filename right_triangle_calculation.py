import math
# рассчёт параметров прямоугольного треугольника
print("""Для входных данных используется два любых параметра в прямоугольном треугольнике,
углы вводятся последовательно - градусы, минуты, секунды. 
В качестве неизвестного проставляется - 0""")
print("""For input data, any two parameters in a right-angled triangle are used,
angles are entered sequentially - degrees, minutes, seconds.
As an unknown, - 0 is affixed""")


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
print('data entered (данные ввели)')
# рассчёт третьей стороны по двум известным
if a != 0 and b != 0 and c == 0:
    c = math.sqrt(a ** 2 + b ** 2)
elif a != 0 and b == 0 and c != 0:
    b = math.sqrt(c ** 2 - a ** 2)
elif a == 0 and b != 0 and c != 0:
    a = math.sqrt(c ** 2 - b ** 2)

# перевод градусов в десятичное значение
a_decimal = a_degrees + a_minutes / 60.0 + a_seconds / 3600.0
b_decimal = b_degrees + b_minutes / 60.0 + b_seconds / 3600.0

# перевод углов в радианы

rad_alfa = math.radians(a_decimal)
rad_betta = math.radians(b_decimal)

# расчёт противоположного угла при одном из известных (в радианах)

if rad_alfa != 0 and rad_betta == 0:
    rad_betta = math.radians(90) - rad_alfa
if rad_betta != 0 and rad_alfa == 0:
    rad_alfa = math.radians(90) - rad_betta

# расчёт сторон при условии что, известны угол и одна из сторон
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
if rad_alfa == 0 and rad_betta == 0:
    rad_alfa = math.asin(a / c)

    rad_betta = math.acos(a / c)

a_degrees_pr = math.degrees(rad_alfa)
#a_degrees_pr = round(a_degrees_pr, 40)
b_degrees_pr = math.degrees(rad_betta)
#b_degrees_pr = round(b_degrees_pr, 40)
print("Leg a (Катет a)",a,'\n'"Leg b (Катет b)",b,'\n'"Hypotenuse (Гипотенуза)",c)
print('Angle alpha in degrees (Угол альфа в градусах)',a_degrees_pr,'\n' "Angle beta in degrees (Угол бетта в градусах)",b_degrees_pr,)
