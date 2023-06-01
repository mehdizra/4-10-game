def prnts_ok(p1, p2, p3, p4, p5, p6):
    if p3 == ')' and p4 == '(': return False
    if p2 == '(' and p3 == ')': return False
    if p4 == '(' and p5 == ')': return False
    if p1 == '(' and p6 == ')': return False
    if p1 == '(' and p2 == '(': return False
    if p2 == '(' and p4 == '(': return False
    if p1 == '(' and p4 == '(': return False
    if p3 == ')' and p5 == ')': return False
    if p3 == ')' and p6 == ')': return False
    if p5 == ')' and p6 == ')':
        return False
    else:
        return True


def statmnt_ok(string):
    if string.find('/0') > 0: return False  # division by zero    
    if '(' not in string and ')' not in string: return True  # without pranthes
    if ')' in string and '(' not in string: return False  # only 1 peranthes
    if '(' in string and ')' not in string: return False  # only 1 peranthes
    if string[1] in '+*': return False  # repeated result
    if string[4] in '*' and string[0] == '(' and string[6] == ')':  # repeated result
        return False
    else:
        return True


def enter_number():
    while True:
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


oprsign = '+-/*'
while True:
    Num_as_list = enter_number()
    digits = len(Num_as_list)  # Convert to 4 separate digits in a list
    resultlist = []
    resultlist1 = []
    unique = dict()  # save all numbers in this dictionary
    cnt = 1  # شمارنده جوابها
    NM = []
    mathex = []
    for i1 in range(0, digits):
        for i2 in range(0, digits):
            for i3 in range(0, digits):
                for i4 in range(0, digits):
                    if len({i1,i2,i3,i4}) != digits: continue
                    NM = [Num_as_list[i1], Num_as_list[i2], Num_as_list[i3], Num_as_list[i4]]
# To prevent repeated calculations in four-digit numbers that contain one or more repeated numbers
                    NM_str = ''.join(str(s) for s in NM).replace(' ', '')
                    if NM_str in unique: 
                        continue
                    else:
                        unique[NM_str] = None 
                        for prnts1 in ' (':  # add parentheses
                            for prnts2 in ' (':
                                for prnts3 in ' )':
                                    for prnts4 in ' (':
                                        for prnts5 in ' )':
                                            for prnts6 in ' )':
                                                if prnts_ok(prnts1, prnts2, prnts3, prnts4, prnts5, prnts6) is False:
                                                    continue
                                                else: # Test 4 main operations between 4 digits and calculate its result
                                                    for op1 in oprsign:
                                                        for op2 in oprsign:
                                                            for op3 in oprsign:
                                                                mathex = [prnts1, NM[0], op1, prnts2, NM[1], prnts3,
                                                                          op2, prnts4, NM[2], prnts5, op3, NM[3],
                                                                          prnts6]
                                                                mathex_str = ''.join(str(e) for e in mathex).replace(
                                                                    ' ', '')
                                                                if statmnt_ok(mathex_str):
                                                                    try:
                                                                        if eval(mathex_str) == 10:
                                                                            mathex_str = str(mathex_str.replace('*', '×').replace('/', '÷') + '=10')
                                                                            if '(' in mathex_str:  #add results in 2 kind of list for sorting
                                                                                resultlist.append(''.join(mathex_str))
                                                                            else:
                                                                                resultlist1.append(''.join(mathex_str))
                                                                        else:
                                                                            continue
                                                                    except:
                                                                        continue
                                                                else:
                                                                    continue
    resultlist.sort()
    resultlist1.sort()
    resultlist1.extend(resultlist)
    if len(resultlist1) == 0:
        print("this number cannot convert to 10")
    else:
        for i in range(len(resultlist1)):
            print(i+1, resultlist1[i])
