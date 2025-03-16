day = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
days = input("Enter a day of the week: ").strip()

if days in day:
    index = day.index(days)
    print(day[index - 1])
    print(day[index + 1])
else:
    print("no")


nums = [1,2,2,2,3,3,4,1,5,9]
nums = set(nums)
print(nums)

num1 = {1,2,3,4,5,6,7,8,9,10}
num2 = {1,2,3,4,8,45,63,41,78,10}
num1 = set(num1)
print(num1.issubset(num2))