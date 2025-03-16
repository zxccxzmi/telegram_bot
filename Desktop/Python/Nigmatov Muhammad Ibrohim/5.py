"""
5.Masala. 30 bal.
    Shahar jamoat transportida avtobuslar list shaklida berilgan. Har bir element (avtobus) dict shaklida bo'lib,
    [{"10": 30}, {"25": 50}, {"48": 20}] вЂ” har biri avtobus raqami va bo'sh joylar sonini bildiradi.
    Vazifalar:
    Foydalanuvchi avtobus raqamini kiritadi.
    Agar avtobus topilsa va bo'sh joy bo'lsa, "Sizga joy bor" deb chiqsin va bo'sh joy 1 taga kamaytirilgan holatda list yangilansin.
    Agar joy bo'lmasa, "Bu avtobus to'la" chiqsin.
    Agar avtobus yo'q bo'lsa, "Bunday avtobus yo'q" chiqsin.
    """

buses = [{"10": 30}, {"25": 50}, {"48": 20}]
bus_number = input("avtobus raqamini kiriting: ")

found = False
for bus in buses:
   if bus_number in bus:
    found = True
    if bus[bus_number] > 0:
        bus[bus_number] -= 1
    else:
        print("bu avtobus to'la")
    break
if not found:
    print("bunday avtobus yo'q")

print("yangi avtobus info:", buses)