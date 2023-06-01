# op = ['x','÷','+','-'] Mathematical operators respectively
def oprate(num1, o, num2):  #Computational function of operands
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

def sign(n):  # change oprators for print
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
    while True:  # input 4 digit numbers correctly
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

while True:  # Convert to 4 separate digits in a list
    Num_as_list = enter_number()
    i = len(Num_as_list)
    result = 0
    new_num = []
    unique = []
    count = 0
    for i1 in range(0, i):  # Extracting different 4-digit numbers from a 4-digit number
        for i2 in range(0, i):
            for i3 in range(0, i):
                for i4 in range(0, i):
                    if len({i1,i2,i3,i4}) != i :
                        continue
                    new_num = [Num_as_list[i1], Num_as_list[i2], Num_as_list[i3], Num_as_list[i4]]
                    if new_num in unique: #To avoid duplicate calculations
                        continue
                    else:
                        unique.append([Num_as_list[i1], Num_as_list[i2], Num_as_list[i3], Num_as_list[i4]])
                    for opr1 in range(0, 4):  # Test 4 main operations between 4 digits and calculate its result
                        for opr2 in range(0, 4):
                            for opr3 in range(0, 4):
                                result = oprate(new_num[0], opr1, new_num[1])
                                result = oprate(result, opr2, new_num[2])
                                result = oprate(result, opr3, new_num[3])
                                if result == 10:  
                                    count += 1  # Calculate the number of discovered paths
                                    print(count, ":  ", new_num[0], sign(opr1), new_num[1], sign(opr2), new_num[2],
                                          sign(opr3), new_num[3], sign(4), int(result))
    if count == 0:
        print("this number cannot convert to 10")
