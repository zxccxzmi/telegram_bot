# import telebot
# import threading
# import time
# import schedule
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# TOKEN = "7714818840:AAFq8OVhLPr9kU6EHf6RrsVMBBElfvFJluo"
# bot = telebot.TeleBot(TOKEN)
#
# # 📚 O'quvchilar va kurslar (user_id: kurs)
# students = {
#     123456789: "course_1",
#     987654321: "course_2",
#     567890123: "course_3",
# }
#
# # 📆 Dars jadvali (kurs: vaqt)
# schedule_data = {
#     "course_1": "09:00",
#     "course_2": "14:00",
#     "course_3": "18:00",
# }
#
# # 👨‍🏫 O‘qituvchi yoki admin ID'si (Bu yerga admin yoki o‘qituvchi ID sini qo‘ying)
# ADMIN_ID = 7442097952
#
#
# # 📌 Asosiy menyu
# def main_menu(message):
#     markup = InlineKeyboardMarkup()
#     btn1 = InlineKeyboardButton("📚 Qo‘shimcha darslar", callback_data="extra_lessons")
#     btn2 = InlineKeyboardButton("📆 Dars jadvali", callback_data="schedule")
#     btn3 = InlineKeyboardButton("📝 Yakuniy imtihon", callback_data="final_exam")
#     btn4 = InlineKeyboardButton("📂 Uy ishi va dars fayllari", callback_data="homework")
#     markup.add(btn1, btn2)
#     markup.add(btn3, btn4)
#     bot.send_message(message.chat.id, "📚 Excel Masters kurslar botiga xush kelibsiz!\nQuyidagilardan birini tanlang:",
#                      reply_markup=markup)


# # 📌 Kurs tanlash
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     if message.chat.id not in students:
#         markup = InlineKeyboardMarkup()
#         markup.add(InlineKeyboardButton("📘 Kurs 1", callback_data="course_1"))
#         markup.add(InlineKeyboardButton("📗 Kurs 2", callback_data="course_2"))
#         markup.add(InlineKeyboardButton("📙 Kurs 3", callback_data="course_3"))
#         bot.send_message(message.chat.id, "🎓 Iltimos, kursingizni tanlang:", reply_markup=markup)
#     else:
#         main_menu(message)
#
#
# @bot.callback_query_handler(func=lambda call: call.data.startswith("course_"))
# def set_course(call):
#     students[call.message.chat.id] = call.data
#     bot.send_message(call.message.chat.id, f"✅ Siz {call.data.replace('_', ' ')} kursini tanladingiz!")
#     main_menu(call.message)
#
#
# # 📆 Dars jadvali
# @bot.callback_query_handler(func=lambda call: call.data == "schedule")
# def show_schedule(call):
#     course = students.get(call.message.chat.id, None)
#     if course and course in schedule_data:
#         bot.send_message(call.message.chat.id, f"📆 Dars vaqti: {schedule_data[course]}")
#     else:
#         bot.send_message(call.message.chat.id, "⏳ Sizda dars jadvali yo‘q.")
#
#
# # 📚 Qo‘shimcha darslar va testlar
# @bot.callback_query_handler(func=lambda call: call.data == "extra_lessons")
# def extra_lessons(call):
#     bot.send_message(call.message.chat.id, "📚 Bu yerda qo‘shimcha darslar va testlar bo‘ladi!")
#
#
# # 📂 Uy ishi va dars fayllari
# @bot.callback_query_handler(func=lambda call: call.data == "homework")
# def homework(call):
#     bot.send_message(call.message.chat.id, "📂 Bu yerda uy ishi va dars materiallari bo‘ladi!")
#
#
# # 📝 Yakuniy imtihon (vaqt, ball tekshirish, sertifikat)
# @bot.callback_query_handler(func=lambda call: call.data == "final_exam")
# def final_exam(call):
#     bot.send_message(call.message.chat.id,
#                      "📝 Sizda yakuniy imtihon boshlanmoqda. 10 daqiqa ichida tugatishingiz kerak!")
#     time.sleep(5)  # 5 soniya kutish (aslida bu yerda haqiqiy test bo‘lishi kerak)
#
#     # Ball chiqarish
#     score = 85  # (bu yerda random ball yoki haqiqiy test natijalari bo‘lishi mumkin)
#     if score >= 80:
#         bot.send_message(call.message.chat.id,
#                          "🎉 Tabriklaymiz! Siz imtihondan o‘tdingiz! Sertifikatingiz PDF shaklda tayyorlanmoqda.")
#         bot.send_document(call.message.chat.id, open("certificate.pdf", "rb"))
#     else:
#         bot.send_message(call.message.chat.id,
#                          "❌ Afsuski, siz imtihondan o‘ta olmadingiz. Qaytadan topshirishga harakat qiling!")
#
#
# # 📢 Eslatma yuborish va tugmalar chiqarish
# def send_schedule_reminders():
#     for user_id, course in students.items():
#         if course in schedule_data:
#             lesson_time = schedule_data[course]
#
#             # Tugmalar
#             markup = InlineKeyboardMarkup()
#             btn1 = InlineKeyboardButton("✅ Men darsga boraman", callback_data=f"yes_{user_id}")
#             btn2 = InlineKeyboardButton("❌ Men ertaga bora olmayman", callback_data=f"no_{user_id}")
#             markup.add(btn1, btn2)
#
#             # Xabar yuborish
#             message = f"📢 *Hurmatli o‘quvchi!*\n\nErtaga soat *{lesson_time}* da darsingiz bor. Iltimos, esdan chiqmasin!"
#             bot.send_message(user_id, message, reply_markup=markup, parse_mode="Markdown")
#
#
# # 🔄 Callback handler
# @bot.callback_query_handler(func=lambda call: call.data.startswith("yes_") or call.data.startswith("no_"))
# def callback_handler(call):
#     user_id = int(call.data.split("_")[1])
#
#     if call.data.startswith("yes_"):
#         bot.send_message(user_id, "✅ Darsga borishingizni tasdiqladingiz!")
#
#     elif call.data.startswith("no_"):
#         msg = bot.send_message(user_id, "❗ Iltimos, darsga bora olmaslik sababini yozing:")
#         bot.register_next_step_handler(msg, send_absence_reason, user_id)
#
#
# # 📩 Foydalanuvchi sababi adminlarga yuboriladi
# def send_absence_reason(message, user_id):
#     reason = message.text
#     bot.send_message(ADMIN_ID,
#                      f"📢 *E'lon!*\n\n👤 {message.from_user.full_name} ({user_id}) ertaga darsga bora olmaydi.\n\n✍ Sabab: {reason}",
#                      parse_mode="Markdown")
#     bot.send_message(user_id, "✅ Sababingiz qabul qilindi va o‘qituvchiga yetkazildi!")
#
#
# # ⏳ Har kuni soat 20:00 da eslatmani yuborish
# schedule.every().day.at("20:00").do(send_schedule_reminders)
#
#
# # 🕒 Schedule loop (bot doimiy ishlashi uchun)
# def schedule_loop():
#     while True:
#         schedule.run_pending()
#         time.sleep(60)
#
#
# # 🔄 Schedule thread
# threading.Thread(target=schedule_loop).start()
#
# # 🔄 Botni doimiy ishlash rejimiga qo‘yish
# bot.polling(none_stop=True)



#
# import telebot
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# TOKEN = "YOUR_BOT_TOKEN"
# bot = telebot.TeleBot(TOKEN)
#
# # 📌 O‘quvchilarning kurslarini saqlash
# students = {}
#
# # 📌 Kurslar ro‘yxati
# courses = ["Komp Savodxonligi", "Excel Boshlang‘ich", "Excel Pro", "Excel Pro Max"]
#
# # 📌 Asosiy menyu
# def main_menu():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("📚 Qo‘shimcha darslar", callback_data="select_kurs_darslar"))
#     markup.add(InlineKeyboardButton("📆 Dars jadvali", callback_data="select_kurs_jadval"))
#     markup.add(InlineKeyboardButton("🎓 Imtihon", callback_data="select_kurs_imtihon"))
#     markup.add(InlineKeyboardButton("📝 Uy vazifalari", callback_data="select_kurs_uy_ishi"))
#     return markup
#
# # 📌 Kurs tanlash menyusi
# def kurs_menu(prefix):
#     markup = InlineKeyboardMarkup()
#     for kurs in courses:
#         markup.add(InlineKeyboardButton(kurs, callback_data=f"{prefix}_{kurs}"))
#     return markup
#
# # 🚀 Start komandasi
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id,
#                      f"Assalomu alaykum, {message.from_user.first_name}!\n\n"
#                      "Quyidagi bo‘limlardan birini tanlang:",
#                      reply_markup=main_menu())
#
# # 📌 Har bir bo‘limga kirganda kurs tanlash
# @bot.callback_query_handler(func=lambda call: call.data.startswith("select_kurs_"))
# def ask_course(call):
#     section = call.data.replace("select_kurs_", "")
#     bot.send_message(call.message.chat.id,
#                      "Iltimos, kursingizni tanlang:",
#                      reply_markup=kurs_menu(section))
#
# # 📚 Qo‘shimcha darslar – Kurs tanlanganidan keyin
# @bot.callback_query_handler(func=lambda call: call.data.startswith("darslar_"))
# def darslar(call):
#     kurs = call.data.replace("darslar_", "")
#     students[call.message.chat.id] = kurs
#     bot.send_message(call.message.chat.id,
#                      f"📖 {kurs} kursi uchun qo‘shimcha dars materiallari va testlar.",
#                      reply_markup=back_button())
#
# # 📆 Dars jadvali – Kurs tanlanganidan keyin
# @bot.callback_query_handler(func=lambda call: call.data.startswith("jadval_"))
# def jadval(call):
#     kurs = call.data.replace("jadval_", "")
#     students[call.message.chat.id] = kurs
#     bot.send_message(call.message.chat.id,
#                      f"📅 {kurs} kursining dars jadvali:\n\n"
#                      "🕒 Dars vaqti: Aniqlanmagan\n"
#                      "⏳ Davomiylik: 1 oy",
#                      reply_markup=back_button())
#
# # 🎓 Imtihon – Kurs tanlanganidan keyin
# @bot.callback_query_handler(func=lambda call: call.data.startswith("imtihon_"))
# def imtihon(call):
#     kurs = call.data.replace("imtihon_", "")
#     students[call.message.chat.id] = kurs
#     bot.send_message(call.message.chat.id,
#                      f"📝 {kurs} kursi uchun imtihonni boshlash uchun quyidagi tugmani bosing:",
#                      reply_markup=InlineKeyboardMarkup().add(
#                          InlineKeyboardButton("🚀 Imtihonni boshlash", callback_data=f"start_exam_{kurs}")
#                      ))
#
# # 📝 Imtihonni boshlash
# @bot.callback_query_handler(func=lambda call: call.data.startswith("start_exam_"))
# def start_exam(call):
#     kurs = call.data.replace("start_exam_", "")
#     bot.send_message(call.message.chat.id,
#                      f"⏳ {kurs} kursi uchun imtihon boshlandi! Sizda 10 daqiqa vaqt bor.")
#
#     import time
#     time.sleep(10)  # Sinov uchun vaqt
#
#     ball = 85  # Test uchun ball
#     if ball >= 80:
#         bot.send_message(call.message.chat.id,
#                          f"✅ {kurs} kursining imtihonidan o‘tdingiz!\n\n"
#                          "📜 Adminlarga uchrashsangiz, sizga sertifikat beriladi.")
#     else:
#         bot.send_message(call.message.chat.id,
#                          f"❌ {kurs} kursining imtihonidan o‘ta olmadingiz.\n\n"
#                          "Keyingi safar yaxshiroq tayyorgarlik ko‘ring!")
#
# # 📝 Uy vazifalari – Kurs tanlanganidan keyin
# @bot.callback_query_handler(func=lambda call: call.data.startswith("uy_ishi_"))
# def uy_ishi(call):
#     kurs = call.data.replace("uy_ishi_", "")
#     students[call.message.chat.id] = kurs
#     bot.send_message(call.message.chat.id,
#                      f"📌 {kurs} kursiga tegishli uy vazifalari va sinf ishlari bo‘limi.",
#                      reply_markup=back_button())
#
# # ⬅️ Orqaga tugmasi
# def back_button():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("⬅️ Orqaga", callback_data="back"))
#     return markup
#
# @bot.callback_query_handler(func=lambda call: call.data == "back")
# def back(call):
#     bot.send_message(call.message.chat.id, "Bosh menyuga qaytdingiz:", reply_markup=main_menu())
#
# # Botni ishga tushirish
# bot.polling()




# import telebot
# import threading
# import time
# import schedule
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# TOKEN = "7714818840:AAFq8OVhLPr9kU6EHf6RrsVMBBElfvFJluo"
# bot = telebot.TeleBot(TOKEN)
#
# # 📌 O‘quvchilarning kurslarini saqlash
# students = {}
#
# # 📌 Kurslar ro‘yxati
# courses = ["Kompyuter Savodxonligi", "Excel Boshlang‘ich", "Excel Pro", "Excel Pro Max"]
#
# # 📌 Dars jadvali (kurs: vaqt)
# schedule_data = {
#     "Kompyuter Savodxonligi": "09:00",
#     "Excel Boshlang‘ich": "14:00",
#     "Excel Pro": "16:00",
#     "Excel Pro Max": "18:00",
# }
#
# # 📌 Asosiy menyu
# def main_menu():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("📚 Qo‘shimcha darslar", callback_data="select_kurs_darslar"))
#     markup.add(InlineKeyboardButton("📆 Dars jadvali", callback_data="select_kurs_jadval"))
#     markup.add(InlineKeyboardButton("🎓 Imtihon", callback_data="select_kurs_imtihon"))
#     markup.add(InlineKeyboardButton("📝 Uy vazifalari", callback_data="select_kurs_uy_ishi"))
#     return markup
#
# # 📌 Kurs tanlash menyusi
# def kurs_menu(prefix):
#     markup = InlineKeyboardMarkup()
#     for kurs in courses:
#         markup.add(InlineKeyboardButton(kurs, callback_data=f"{prefix}_{kurs}"))
#     return markup
#
# # 🚀 Start komandasi
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id,
#                      f"Assalomu alaykum, {message.from_user.first_name}!\n\n"
#                      "Siz hozirda qaysi kursda o‘qimoqdasiz? Tanlang:",
#                      reply_markup=kurs_menu("select"))
#
# # 📌 Kursni tanlagandan keyingi jarayon
# @bot.callback_query_handler(func=lambda call: call.data.startswith("select_"))
# def select_kurs(call):
#     kurs = call.data.split("_")[1]
#     students[call.from_user.id] = kurs
#     bot.send_message(call.message.chat.id,
#                      f"Siz **{kurs}** kursini tanladingiz!\n\n"
#                      "Asosiy menyudan kerakli bo‘limni tanlang:",
#                      reply_markup=main_menu())
#
# # 📌 Dars jadvalini avtomatik eslatish
# def send_schedule_reminder():
#     for user_id, kurs in students.items():
#         if kurs in schedule_data:
#             bot.send_message(user_id,
#                              f"📢 *Hurmatli o‘quvchi!* \n\n"
#                              f"Sizning ertaga soat {schedule_data[kurs]} da darsingiz bor. Iltimos, esdan chiqarmang!",
#                              reply_markup=dars_qatnashuv_tugmalar())
#
# # 📌 Darsga borish yoki bormaslik tugmalari
# def dars_qatnashuv_tugmalar():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("✅ Men darsga boraman", callback_data="dars_ha"))
#     markup.add(InlineKeyboardButton("❌ Men ertaga darsga bora olmayman", callback_data="dars_yoq"))
#     return markup
#
# # 📌 Darsga qatnashish haqida javobni qabul qilish
# @bot.callback_query_handler(func=lambda call: call.data.startswith("dars_"))
# def dars_qatnashuv(call):
#     user_id = call.from_user.id
#     if call.data == "dars_ha":
#         bot.send_message(user_id, "✅ Darsga borishingiz qayd etildi. Rahmat!")
#     elif call.data == "dars_yoq":
#         bot.send_message(user_id, "❗ Iltimos, sababini yozing:")
#         bot.register_next_step_handler(call.message, sabab_qabul)
#
# # 📌 Sababni qabul qilish va adminlarga yuborish
# def sabab_qabul(message):
#     admin_id = " 7442097952"  # Bu yerga admin ID sini qo‘ying
#     bot.send_message(admin_id, f"📢 *O‘quvchi {message.from_user.first_name} darsga bora olmaydi!* \n\nSabab: {message.text}")
#     bot.send_message(message.chat.id, "Sizning sababingiz adminga yuborildi.")
#
# # 📌 Imtihon jarayoni
# @bot.callback_query_handler(func=lambda call: call.data.startswith("select_kurs_imtihon"))
# def imtihon_boshlash(call):
#     user_id = call.from_user.id
#     if user_id not in students:
#         bot.send_message(user_id, "Siz hali kurs tanlamagansiz! Iltimos, avval kursni tanlang.")
#         return
#     bot.send_message(user_id, "⏳ Imtihon boshlanmoqda! Sizda 10 daqiqa vaqt bor. Tayyor bo‘ling!")
#     # Bu yerda test savollari bo‘lishi mumkin (hozircha yo‘q)
#     time.sleep(600)  # 10 daqiqa kutish (real imtihonda boshqacha bo‘ladi)
#     bot.send_message(user_id, "⏳ Imtihon vaqti tugadi! Natijalar tekshirilmoqda...")
#     ball = 85  # Tasodifiy ball (real imtihonda foydalanuvchidan olinadi)
#     if ball >= 80:
#         bot.send_message(user_id,
#                          f"🎉 Tabriklaymiz! Siz {ball} ball bilan imtihondan o‘tdingiz.\n\n"
#                          "Sertifikat olish uchun administrator bilan bog‘laning.")
#     else:
#         bot.send_message(user_id,
#                          f"😔 Afsuski, siz {ball} ball oldingiz va imtihondan o‘tmadingiz.\n\n"
#                          "Qayta topshirish uchun administrator bilan bog‘laning.")
#
# # 📌 Schedule ni ishlatish uchun alohida thread
# def schedule_checker():
#     while True:
#         schedule.run_pending()
#         time.sleep(60)
#
# # 📌 Har kuni 21:00 da dars eslatmalarini yuborish
# schedule.every().day.at("21:00").do(send_schedule_reminder)
#
# # 📌 Thread orqali schedule ni ishga tushirish
# threading.Thread(target=schedule_checker, daemon=True).start()
#
# # 📌 Botni ishga tushirish
# bot.polling()


import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7714818840:AAFq8OVhLPr9kU6EHf6RrsVMBBElfvFJluo"
bot = telebot.TeleBot(TOKEN)

# 📚 O'quvchilar va kurslar (user_id: kurs)
students = {}


# 📌 Asosiy menyu
def main_menu(chat_id):
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("📚 Qo‘shimcha darslar", callback_data="extra_lessons")
    btn2 = InlineKeyboardButton("📆 Dars jadvali", callback_data="schedule")
    btn3 = InlineKeyboardButton("📝 Yakuniy imtihon", callback_data="final_exam")
    btn4 = InlineKeyboardButton("📂 Uy ishi va dars fayllari", callback_data="homework")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)

    bot.send_message(chat_id, "📚 Excel Masters kurslar botiga xush kelibsiz!\nQuyidagilardan birini tanlang:",
                     reply_markup=markup)


# 📌 Kurs tanlash
@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.id not in students:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("📘 Kurs 123", callback_data="course_123"))
        markup.add(InlineKeyboardButton("📗 Kurs 456", callback_data="course_456"))
        markup.add(InlineKeyboardButton("📙 Kurs 789", callback_data="course_789"))
        bot.send_message(message.chat.id, "🎓 Iltimos, kursingizni tanlang:", reply_markup=markup)
    else:
        main_menu(message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("course_"))
def set_course(call):
    students[call.message.chat.id] = call.data  # Foydalanuvchini lug‘atga qo‘shish
    bot.send_message(call.message.chat.id, f"✅ Siz {call.data.replace('_', ' ')} kursini tanladingiz!")
    main_menu(call.message.chat.id)  # Asosiy menyuni ochish


# 📆 Dars jadvali
@bot.callback_query_handler(func=lambda call: call.data == "schedule")
def show_schedule(call):
    bot.send_message(call.message.chat.id, "📆 Bu yerda dars jadvali bo‘ladi!")


# 📚 Qo‘shimcha darslar
@bot.callback_query_handler(func=lambda call: call.data == "extra_lessons")
def extra_lessons(call):
    bot.send_message(call.message.chat.id, "📚 Bu yerda qo‘shimcha darslar bo‘ladi!")


# 📂 Uy ishi va dars fayllari
@bot.callback_query_handler(func=lambda call: call.data == "homework")
def homework(call):
    bot.send_message(call.message.chat.id, "📂 Bu yerda uy ishi va dars materiallari bo‘ladi!")


# 📝 Yakuniy imtihon
@bot.callback_query_handler(func=lambda call: call.data == "final_exam")
def final_exam(call):
    bot.send_message(call.message.chat.id, "📝 Yakuniy imtihon haqida ma'lumot bu yerda bo‘ladi!")


# 🔄 Botni doimiy ishlash rejimiga qo‘yish
bot.polling(none_stop=True)
