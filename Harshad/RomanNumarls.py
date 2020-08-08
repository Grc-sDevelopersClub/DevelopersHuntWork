def Roman_no(num):
    roman_no = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX"
               ,70:"LXX",80:"LXXX",90:"XC",100:"C"}
    ls_no = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]
    once = num % 10
    tense = num - once
    if num in ls_no:
        return roman_no[num]
    else:
        return roman_no[tense] + roman_no[once]

def main():
    number = input(">> ")
    len_num = len(number)
    ls_distinct = []
    for i in range(len_num):
        if number[i] not in ls_distinct:
            ls_distinct.append(number[i])

    len_ls_dis = len(ls_distinct)
    result = Roman_no(len_ls_dis)
    print(result)

no_test_case = int(input("no_test_case: "))
for i in range(no_test_case):
    main()
    
