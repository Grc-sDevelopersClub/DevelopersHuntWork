print("enter x to exit the programme")
print("enter three numbers yo want")
num1=int(input("enter 1st number:"))
if num1 =="x":
    exit()
else:
    num1=int(num1)
    num2=int(input("enter 2nd number:"))
    num3=int(input("enter 3rd number"))
    largest=num1
    if largest < num2:
        if num2 > num3:
            largest=num2

        else :
                 largest = num3
    elif largest < num3:
        if num3 > num2:
            largest = num3
        else:
            largest= num2
    else:
       largest = num1

    if(num1==num2 and num2==num3):
        print("All the three numbers are equal")
    else:
        print("largest number is " + str(largest))





