"""
3.Masala. 20 bal.
    Talabalar imtihondan olingan ballari list shaklida berilgan.

    grades = [45, 78, 90, 65, 88, 55, 92, 70]  

    Eng yuqori va eng past ballni toping.
    O'rtacha ballni hisoblang.
    70 dan yuqori ball olganlarni yangi list ga joylang.
"""

grades = [45, 78, 90, 65, 88, 55, 92, 70]

highest_score = max(grades)
lowest_score = min(grades)

total = 0

for i in grades:
    total += i

average = total / len(grades)

new_grades = []
for i in grades:
    if i > 70:
        new_grades.append(i)

print(f"The highest score is {highest_score}")
print(f"The lowest score is {lowest_score}")
print(f"The average is {average}")
print(f"Above 70 are: {new_grades}")