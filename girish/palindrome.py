#program to check whether the string is palindromic or not.....
input_string = input("enter the string to check palindrome:")
if input_string == input_string[::-1]:
    print("The Given String Is PALINDROMIC")
else:
    print("the Given string is not palindromic")