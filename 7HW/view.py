import string

def get_system():
        sys_mean = int(input('Input the tupe of your number: 1 - complex, 2 - ratio'))
        return sys_mean

def get_r_value():
    value_a = float(input('value_a = '))
    value_b = float(input('value_b = '))
    return value_a, value_b

def get_c_value():
    value_a = string(input('value_a = '))
    value_b = string(input('value_b = '))
    return value_a, value_b

def get_mode():
    mode = input('please, input your operation ("/", "+", "*", "-"): ')
    if mode.lower() == '/':
            return 1
    elif mode.lower() == '*':
            return 4
    elif mode.lower() == '+':
            return 3
    elif mode.lower() == '-':
            return 2
    else:
        print("input right operator ("/", "+", "*", "-")")
    

mode = {1: 'devision of', 4: 'mult of', 3: 'sum of', 2: 'substraction of'}
def return_result(res, oper):
    return f'result of operation {mode[oper]} = {res}'
