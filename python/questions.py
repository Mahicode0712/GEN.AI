try:
    num1=float(input("enter the number: "))
    num2=float(input("enter the number: "))


    result = num1/num2
    print("the result is " , result)

except ZeroDivisionError:
    print("Error : the division from zero is not defined ")
print(" try again ")        