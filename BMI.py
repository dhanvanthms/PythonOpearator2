height=float(input("enter you're height in centimeters "))
weight=float (input ("enter you're weight in killograms "))
bmi=weight/(height/100)**2
print("you're bmi is",bmi)
if bmi <=18.5:
    print("you are under weight")
elif bmi <=25:
    print("you are healthy")
elif bmi<=30:
    print("you are over weight")
elif bmi>=30:
    print("you are obiese")
else:
    print("you're input is wrong")