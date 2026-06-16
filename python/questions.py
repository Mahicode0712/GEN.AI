# try:
#     num1=float(input("enter the number: "))
#     num2=float(input("enter the number: "))


#     result = num1/num2
#     print("the result is " , result)

# except ZeroDivisionError:
#     print("Error : the division from zero is not defined ")
# print(" try again ")        

#invalid integer
try:

   num = int(input("enter the number: "))
   print("you entered the number : " , num)
except ValueError:
        print("enter a valid number")



