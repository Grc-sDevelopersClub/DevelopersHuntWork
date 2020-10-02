def fact(no):
    if no == 1:
        return 1
    else:
        return no * fact(no - 1)
def add_digit(number):
    type_cast = str(number)
    len_number = len(type_cast)
    ls_digits = []
    for i in range(len_number):
        ls_digits.append(int(type_cast[i]))

    summition = sum(ls_digits)
    return summition

def main():
    input_digit = int(input(">> "))
    actual_num = fact(input_digit)
    result = add_digit(actual_num)
    print(result)

main()
