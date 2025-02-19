y=int(input("Enter a Number"))
if y%2 == 0:
    if y%3 == 0:
       print("divisible both by 2 and 3")
    else:
       print("divisible by 2 but not 3")  
elif y<3:
    print("less than 3")
else:
    print("ODD")        
bmi = round(y/3)
print(bmi)
