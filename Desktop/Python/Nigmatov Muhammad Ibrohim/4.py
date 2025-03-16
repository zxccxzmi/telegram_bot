"""
4.Masala. 25 bal.
Foydalanuvchi matn kiritadi. Dastur ushbu matndagi har bir so'zni faqat bir marta chiqarib,
necha marta takrorlanganini ham ko'rsatib bersin.

Masalan:
input)  text = "salom dunyo salom hammaga dunyo dunyo"
output) salom - 2 marta  
        dunyo - 3 marta  
        hammaga - 1 marta
Yordam: split() yordamida so'zlarni ajratish. dict dan malumotlarni yig'ish uchun ishlatishingiz mumkin
"""

text = input("Enter a text: ")
words = text.split()

for word in set(words):
    print(word, "-", words.count(word), "times")
