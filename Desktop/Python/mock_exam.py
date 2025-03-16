(easy level)


1 - mashq

num = int(input("Enter a num: "))

if num % 2 == 0:
    print("Juft")
else:
    print("Toq")

2 - mashq

num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2nd num: "))
num3 = int(input("Enter 3rd num: "))

print("The biggest num is: ", max(num1,num2,num3))
print("The largest num is: ", min(num1,num2,num3))

3 - mashq

words = input("Enter three words: ").split()
print("The longest word is: ", max(words))

4 - mashq

n = int(input("Enter a num: "))
count = 0
for num in range (1, n + 1):
    count += num
print("Yigindi: ", count)

5 - mashq

nums = (input("Enter three numbers: ")).split()
print("the biggest number is: ", max(nums))


(normal level)


1 - mashq

num = int(input("Enter a num: "))

for i in range(1, num + 1):
    if i % 2 == 0:
        print(i, "Juft")
    else:
        print(i, "Toq")

2 - mashq

num = (input("Enter a num: "))
count = 0
for digit in num:
    count += int(digit)
print("Yigindi: ", count)

3 - mashq

num = (input("Enter a num: "))
reverse_num = num[::-1]
print(reverse_num)

4 - mashq

num = input("Enter a num: ")
even_nums = 0
odd_nums = 0

for digit in num:
    digit = int(digit)
    if digit % 2 == 0:
        even_nums += digit
    else:
        odd_nums += digit
print("Juft: ", even_nums)
print("Toq: ", odd_nums)

5 - mashq

num = input("Enter a num: ")

if list(num) == sorted(num):
    print("Ha")
else:
    print("Yo'q")


(hard level)


