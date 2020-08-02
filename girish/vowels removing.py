def removevowel(newstr,string):
    vowels=('a','e','i','o','u','A','E','I','O','U')

    for c in string:
        if c in vowels:
            newstr= newstr.replace(c,'')
    print("the new string without the vowels is " + newstr)
    return newstr
print("enter any string ou wish to remove the vowels of")
string=input("enter any string you want:")
if string == "x":
    exit()
else:
    newstr=string
    print("we are removing the vowels.........")
    newstr=removevowel(newstr,string)

