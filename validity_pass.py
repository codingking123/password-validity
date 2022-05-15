# NAME: GAURAV YELURE
# ROLL NO: BE20F05F070

import re
password=str(input("Enter a password which you want to check validity:"))
flag=0

while True:
    if (len(password)<8):
        flag=-1
        break
    elif not re.search("[a-z]", password):
        flag=-1
        break
    elif not re.search("[A-Z]", password):
        flag=-1
        break
    elif not re.search("[0-9]", password):
        flag=-1
        break
    elif not re.search("[_@#$]", password):
        flag=-1
        break
    else:
        flag=0
        print("Your password is valid and strong")
        break

if flag==-1:
    print("Your password is invalid and not strong:")
    print("Please Add:")
    print("1.uppercase letter")
    print("2.Lowercase letter")
    print("3.whole number letter")
    print("4.Special symbol")
    print("In your password")