for num in range(2, 20, 2):
    print(num)



word = input("Enter a word: ")
count = int(input("Enter a count: "))
for i in range (count):
    print(word)




N = int(input("Enter a N: "))
S = 0
for i in range(1, N+1):
    S += i

print(S)

num = int(input("Enter a num: "))

for i in range(1, num+1):
    print(f"{i} ning kvadrati: {i * i}")






num = int(input("Enter a num 1 - 10: "))
for i in range(1, 11):
    print(f"{num} * {i} = {i * num}")