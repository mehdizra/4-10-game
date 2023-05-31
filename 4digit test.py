# op = ['x','÷','+','-'] ترتیب عملگراها

def oprate(num1, o, num2):  # تابع محاسبه کننده عملگراها
    if o == 0:
        return num1 * num2
    if o == 1:
        if num2 == 0:
            return 0
        else:
            return num1 / num2
    if o == 2:
        return num1 + num2
    if o == 3:
        return num1 - num2


def sign(n):  # تابع مشخص کننده عملگراها برای چاپ
    if n == 0:
        return 'x'
    if n == 1:
        return '÷'
    if n == 2:
        return '+'
    if n == 3:
        return '-'
    if n == 4:
        return '='


def enter_number():
    while True:  # دریافت عدد درست 4 رقمی
        print('To exit enter 0')
        try:
            inp_number = int(input('Enter a 4 digit number: '))
            if inp_number == 0 or inp_number in range(1000, 10000):
                break
            else:
                continue
        except:
            print('Wrong Entery: ')
    if inp_number == 0:
        quit()
    num_as_list = []
    cntr = 4
    while cntr >= 1:
        num_as_list.append(inp_number % 10)
        inp_number //= 10
        cntr -= 1
    num_as_list.reverse()
    return num_as_list


while True:
    Num_as_list = enter_number()
    # تبدیل به 4 رقم مجزا در یک لیست
    i = len(Num_as_list)
    result = 0
    new_num = []
    unique = []
    count = 0
    for i1 in range(0, i):  # استخراج اعداد 4رقمی مختلف از یک عدد 4 رقمی
        for i2 in range(0, i):
            for i3 in range(0, i):
                for i4 in range(0, i):
                    if i1 == i2 or i1 == i3 or i1 == i4 or i2 == i3 or i2 == i4 or i3 == i4:
                        continue
                    new_num = [Num_as_list[i1], Num_as_list[i2], Num_as_list[i3], Num_as_list[i4]]
                    # برای جلوگیری از محاسبات تکراری در اعداد چهاررقمی که یک یا چند عدد در آنها تکرار شده اند
                    if new_num in unique:
                        continue
                    else:
                        unique.append([Num_as_list[i1], Num_as_list[i2], Num_as_list[i3], Num_as_list[i4]])
                    for opr1 in range(0, 4):  # تست 4 عمل اصلی بین 4 رقم و محاسبه نتیجه آن
                        for opr2 in range(0, 4):
                            for opr3 in range(0, 4):
                                result = oprate(new_num[0], opr1, new_num[1])
                                result = oprate(result, opr2, new_num[2])
                                result = oprate(result, opr3, new_num[3])
                                if result == 10:  # در صورت 10 بودن نتیجه محاسبات، عملگراها چاپ می شوند
                                    count += 1  # محاسبه تعداد راههای کشف شده
                                    print(count, ":  ", new_num[0], sign(opr1), new_num[1], sign(opr2), new_num[2],
                                          sign(opr3), new_num[3], sign(4), int(result))
    if count == 0:
        print("این اعداد به 10 تبدیل نمی شوند")
