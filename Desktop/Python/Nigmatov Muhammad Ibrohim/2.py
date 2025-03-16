"""
2.Masala. 15 bal.
    Foydalanuvchidan ikkita malumotni input sifatida oling, biri uning 
    ismi, ikkinchisi esa shunchaki bir harf. Vazifangiz usha harf ismini 
    ichida nechta ekanligini hisoblab berish. Tekshirishingiz kerak bo'lgan
    narsalar: ism faqat harflardan tashkil topgan bo'lishi kerak, uzunligi kamida
    2 ta belgidan iborat bo'lishi kerak, ikkinchi inputni uzunligi esa faqat
    1 bo'lishi mumkin va u harf bo'lishi shart.
"""

name = input("Enter your name: ")
letter = input("Entet a letter (a,b,c): ")

if not (name.isalpha) and len(name) >= 2:
    print("Invalid, you can use only letters and minimum 2 words! ")
elif not (letter.isalpha) and len(letter) == 1:
    print("Invalid, you should use only 1 letter (a,b,c)! ")
else :
    result = name.lower().count(letter.lower())
    print(f"'{letter}' in '{name}' '{result}' times")