def kalk(num1, num2, plus):
   if num1.isdigit() and num2.isdigit():
       if plus == '+':
           result = int(num1) + int(num2)
       elif plus == '-':
           result = int(num1) - int(num2)
       elif plus == '*':
           result = int(num1) * int(num2)
       elif plus == '/':
           result = int(num1) / int(num2)


    num1 = (input("Enter 1st num: "))
    num2 = (input("Enter 2nd num: "))
    plus = input("Enter a operator +,-,*,/ : ")


kalk()