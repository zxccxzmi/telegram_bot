# import telebot
#
# bot = telebot.TeleBot('7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ')
#
#
# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'Hello':
#         bot.send_message(message, f'Hello, {message.from_user.first_name}')
#     elif message.text.lower() == 'id':
#         bot.send_message(message.chat.id, f'ID: {message.from_user.id}')
#
#
# bot.polling(none_stop=True)

# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
#
# TOKEN = '7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ'
# bot = telebot.TeleBot(TOKEN)
#
# # Foydalanuvchi tugmalari
# def main_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("Kompyuter Savodxonligi"), KeyboardButton("Excel Boshlang'ich"))
#     markup.add(KeyboardButton("Excel Pro"), KeyboardButton("Excel Pro Max"))
#     return markup
#
# # Inline tugmalar
# def get_course_buttons():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("📌 Batafsil ma'lumot", url="https://t.me/info_excel"))
#     markup.add(InlineKeyboardButton("📞 Admin bilan bog'lanish", url="https://t.me/admin_username"))
#     return markup
#
# # Kurs haqida ma'lumotlar
# subject_lessons = {
#     "Kompyuter Savodxonligi": "💻 **Kompyuter Savodxonligi kursi**\n\n📌 Kompyuterning asosiy qismlari\n📌 Dasturiy ta’minotlar\n📌 Internetdan foydalanish\n📌 Foydali klaviatura qisqichlari",
#     "Excel Boshlang'ich": "📊 **Excel Boshlang‘ich kursi**\n\n📌 Excel interfeysi bilan tanishish\n📌 Formulalar va funksiyalar\n📌 Jadval yaratish va dizayni\n📌 Filtr va saralash",
#     "Excel Pro": "📈 **Excel Pro kursi**\n\n📌 Murakkab formulalar\n📌 Power Query va ma’lumotlar tahlili\n📌 Shartli formatlash\n📌 Ma’lumotlar avtomatlashtirish",
#     "Excel Pro Max": "🚀 **Excel Pro Max kursi**\n\n📌 Pivot table va dashboardlar\n📌 Macro va VBA dasturlash\n📌 Katta hajmli ma’lumotlar bilan ishlash"
# }
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f'Assalomu alaykum, {message.from_user.first_name}! \nExcel kurslarimiz haqida ma’lumot olish uchun quyidagi menyudan tanlang:', reply_markup=main_menu())
#
# @bot.message_handler(func=lambda message: message.text in subject_lessons)
# def send_course_info(message):
#     bot.send_message(message.chat.id, subject_lessons[message.text], reply_markup=get_course_buttons())
#
# @bot.message_handler(func=lambda message: message.text.lower() == 'id')
# def send_id(message):
#     bot.send_message(message.chat.id, f'ID: {message.from_user.id}')
#
# bot.polling(none_stop=True)
# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
#
# bot = telebot.TeleBot('7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ')
#
#
# # Bosh menyu tugmalari
# def main_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("📚 Kurslarimiz"), KeyboardButton("👨‍🏫 Mutaxassislarimiz"))
#     markup.add(KeyboardButton("ℹ️ Excel Masters haqida"), KeyboardButton("📞 Biz bilan bog‘lanish"))
#     return markup
#
#
# # Kurs tugmalari
# def course_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("💻 Kompyuter Savodxonligi"), KeyboardButton("📊 Excel Boshlang‘ich"))
#     markup.add(KeyboardButton("📈 Excel Pro"), KeyboardButton("🚀 Excel Pro Max"))
#     markup.add(KeyboardButton("⬅️ Orqaga"))
#     return markup
#
#
# # Mutaxassislar tugmalari
# def teacher_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("Shahzod Sayfulla"), KeyboardButton("Akmaljon X"))
#     markup.add(KeyboardButton("⬅️ Orqaga"))
#     return markup
#
#
# # Kurslar haqida to‘liq ma’lumot
# def get_course_info(course):
#     courses = {
#         "💻 Kompyuter Savodxonligi": "📌 Kurs davomiyligi: 2 oy\n📌 Narxi: 600.000 so‘m\n📌 Dars kunlari: Dushanba, Chorshanba, Juma\n📌 Soat: 10:00 - 12:00\n📌 Yangi guruh: 1-aprel\n\n✅ Kurs yakunida sertifikat beriladi!",
#         "📊 Excel Boshlang‘ich": "📌 Kurs davomiyligi: 3 oy\n📌 Narxi: 800.000 so‘m\n📌 Dars kunlari: Seshanba, Payshanba, Shanba\n📌 Soat: 14:00 - 16:00\n📌 Yangi guruh: 5-aprel\n\n✅ Kurs yakunida sertifikat beriladi!",
#         "📈 Excel Pro": "📌 Kurs davomiyligi: 4 oy\n📌 Narxi: 1.200.000 so‘m\n📌 Dars kunlari: Dushanba, Chorshanba, Juma\n📌 Soat: 16:30 - 18:30\n📌 Yangi guruh: 10-aprel\n\n✅ Kurs yakunida sertifikat beriladi!",
#         "🚀 Excel Pro Max": "📌 Kurs davomiyligi: 5 oy\n📌 Narxi: 1.500.000 so‘m\n📌 Dars kunlari: Seshanba, Payshanba, Shanba\n📌 Soat: 18:30 - 20:30\n📌 Yangi guruh: 15-aprel\n\n✅ Kurs yakunida sertifikat beriladi!"
#     }
#     return courses.get(course, "Bunday kurs mavjud emas!")
#
#
# # Start komandasi
# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id,
#                      f'Assalamu Alaykum hurmatli {message.from_user.first_name}! Excel Masters o‘quv markazining rasmiy Telegram botiga xush kelibsiz!',
#                      reply_markup=main_menu())
#
#
# # Tugmalarga javob berish
# @bot.message_handler(func=lambda message: True)
# def handle_buttons(message):
#     text = message.text
#
#     if text == "📚 Kurslarimiz":
#         bot.send_message(message.chat.id, "Quyidagi kurslardan birini tanlang:", reply_markup=course_menu())
#     elif text in ["💻 Kompyuter Savodxonligi", "📊 Excel Boshlang‘ich", "📈 Excel Pro", "🚀 Excel Pro Max"]:
#         bot.send_message(message.chat.id, get_course_info(text))
#     elif text == "👨‍🏫 Mutaxassislarimiz":
#         bot.send_message(message.chat.id, "Mutaxassislarimizni tanlang:", reply_markup=teacher_menu())
#     elif text == "Shahzod Sayfulla":
#         bot.send_message(message.chat.id,
#                          "👨‍🏫 **Shahzod Sayfulla Begzod o‘g‘li**\n📌 12 yillik MS Excel mutaxassisi (auditor)\n📌 Excel Masters asoschisi\n📌 Tug‘ilgan yili: 07.09.1992")
#     elif text == "ℹ️ Excel Masters haqida":
#         bot.send_message(message.chat.id,
#                          "📌 Excel Masters 2021 yilda tashkil topgan.\n📌 3000 dan ortiq o‘quvchilar muvaffaqiyatli bitirgan.\n📌 Bizda eng tajribali mutaxassislar dars beradi!")
#     elif text == "📞 Biz bilan bog‘lanish":
#         bot.send_message(message.chat.id, "📞 Telefon: +998 90 123 45 67\n📱 Telegram: @ExcelMasters_Admin")
#     elif text == "⬅️ Orqaga":
#         bot.send_message(message.chat.id, "Bosh menyuga qaytdik!", reply_markup=main_menu())
#
#
# bot.polling(none_stop=True)


# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
#
# bot = telebot.TeleBot('7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ')
#
# # Bosh menyu
# main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
# main_menu.add("Kurslarimiz", "Mutaxassislarimiz")
# main_menu.add("Excel Masters haqida", "Biz bilan bog‘lanish")
#
#
# # Kurslar haqida batafsil ma'lumot
# def course_info(course_name):
#     courses = {
#         "Kompyuter Savodxonligi": "💻 *Kompyuter Savodxonligi*\n\n🕒 Davomiyligi: 2 oy\n💰 Narxi: 500 000 so‘m / oy\n📅 Dars kunlari: Dushanba, Chorshanba, Juma\n🕘 Soat: 10:00 - 12:00\n🎓 Kurs yakunida sertifikat beriladi!\n📚 O‘rganasiz: Windows, Office, Internet ishlash",
#         "Excel Boshlang'ich": "📊 *Excel Boshlang‘ich*\n\n🕒 Davomiyligi: 2 oy\n💰 Narxi: 600 000 so‘m / oy\n📅 Dars kunlari: Seshanba, Payshanba, Shanba\n🕘 Soat: 14:00 - 16:00\n🎓 Kurs yakunida sertifikat beriladi!\n📚 O‘rganasiz: Excel asoslari, formulalar, jadval dizayni",
#         "Excel Pro": "📈 *Excel Pro*\n\n🕒 Davomiyligi: 3 oy\n💰 Narxi: 800 000 so‘m / oy\n📅 Dars kunlari: Dushanba, Chorshanba, Juma\n🕘 Soat: 18:00 - 20:00\n🎓 Kurs yakunida sertifikat beriladi!\n📚 O‘rganasiz: Murakkab formulalar, Power Query, shartli formatlash"
#     }
#     return courses.get(course_name, "Bunday kurs mavjud emas")
#
#
# # Mutaxassislar haqida
# teachers = "👨‍🏫 *Mutaxassislarimiz:*\n\n1️⃣ *Shahzod Sayfulla* - 12 yillik MS Excel mutaxassisi\n2️⃣ *Azizbek Xudoyberdiyev* - Data analyst, Excel ekspert\n3️⃣ *Dilshod Rahimov* - VBA va avtomatlashtirish mutaxassisi"
#
# # Excel Masters haqida
# excel_masters_info = "🏫 *Excel Masters Markazi*\n\n📅 Tashkil topgan yili: 2021\n🎓 3000+ bitiruvchi\n📈 MS Excel va IT sohasida eng yaxshi ta'lim markazi!\n\n👨‍💼 *Asoschisi:* Shahzod Sayfulla Begzod o‘g‘li"
#
# # Bog‘lanish
# contact_info = "📞 *Biz bilan bog‘lanish:*\n📱 Telefon: +998 90 123 45 67\n📩 Telegram: @ExcelMasters"
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id,
#                      f'Assalamu alaykum {message.from_user.first_name}! \n\nExcel Masters o‘quv markazining rasmiy botiga xush kelibsiz! \n\nSiz bu yerda kurslarimiz haqida ma’lumot olishingiz mumkin.',
#                      reply_markup=main_menu)
#
#
# @bot.message_handler(func=lambda message: True)
# def message_handler(message):
#     text = message.text
#
#     if text == "Kurslarimiz":
#         markup = ReplyKeyboardMarkup(resize_keyboard=True)
#         markup.add("Kompyuter Savodxonligi", "Excel Boshlang'ich")
#         markup.add("Excel Pro", "🔙 Orqaga")
#         bot.send_message(message.chat.id, "📚 O‘zingizni qiziqtirgan kursni tanlang:", reply_markup=markup)
#
#     elif text in ["Kompyuter Savodxonligi", "Excel Boshlang'ich", "Excel Pro"]:
#         bot.send_message(message.chat.id, course_info(text))
#
#     elif text == "Mutaxassislarimiz":
#         bot.send_message(message.chat.id, teachers)
#
#     elif text == "Excel Masters haqida":
#         bot.send_message(message.chat.id, excel_masters_info)
#
#     elif text == "Biz bilan bog‘lanish":
#         bot.send_message(message.chat.id, contact_info)
#
#     elif text == "🔙 Orqaga":
#         bot.send_message(message.chat.id, "Bosh menyu", reply_markup=main_menu)
#
#     else:
#         bot.send_message(message.chat.id, "❌ Noto‘g‘ri buyruq. Iltimos, menyudan tanlang.")
#
#
# bot.polling(none_stop=True)



# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
#
# bot = telebot.TeleBot('7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ')
#
# # Kurslar haqida batafsil ma'lumot
# courses = {
#     "✨ Kompyuter Savodxonligi": {
#         "info": "💻 **Kompyuter Savodxonligi**\n\nSiz quyidagilarni o'rganasiz:\n✅ Kompyuterning asosiy tushunchalari\n✅ Operatsion tizimlar (Windows)\n✅ Internet va xavfsizlik\n✅ Klaviatura qisqichlari va tezkor usullar\n\n*Davomiyligi:* 2 oy\n*Dars kunlari:* Dushanba, Chorshanba, Juma\n*Soat:* 14:00 - 16:00\n*Narxi:* 600 000 so‘m / oy\n\n⭐ Kurs yakunida sertifikat beriladi!",
#         "video": "computer_savodxonligi.mp4"
#     },
#     "📊 Excel Boshlang'ich": {
#         "info": "📊 **Excel Boshlang'ich**\n\nSiz quyidagilarni o'rganasiz:\n✅ Excel interfeysi va funksiyalari\n✅ Jadval yaratish va tahlil qilish\n✅ Formulalar va asosiy funksiyalar\n✅ Filtr va saralash\n\n*Davomiyligi:* 2 oy\n*Dars kunlari:* Seshanba, Payshanba, Shanba\n*Soat:* 10:00 - 12:00\n*Narxi:* 700 000 so‘m / oy\n\n⭐ Kurs yakunida sertifikat beriladi!",
#         "video": "excel_boshlangich.mp4"
#     },
#     "📈 Excel Pro": {
#         "info": "📈 **Excel Pro**\n\nSiz quyidagilarni o'rganasiz:\n✅ Kengaytirilgan formulalar va Power Query\n✅ Shartli formatlash va avtomatlashtirish\n✅ Dashboardlar va vizualizatsiya\n✅ Katta hajmli ma'lumotlar bilan ishlash\n\n*Davomiyligi:* 3 oy\n*Dars kunlari:* Dushanba, Chorshanba, Juma\n*Soat:* 16:00 - 18:00\n*Narxi:* 900 000 so‘m / oy\n\n⭐ Kurs yakunida sertifikat beriladi!",
#         "video": "excel_pro.mp4"
#     },
#     "💨 Excel Pro Max": {
#         "info": "💨 **Excel Pro Max**\n\nSiz quyidagilarni o'rganasiz:\n✅ VBA dasturlash va makroslar\n✅ Ma'lumotlarni avtomatlashtirish\n✅ Katta hajmli datasetlar bilan ishlash\n✅ Ish faoliyatini optimallashtirish\n\n*Davomiyligi:* 3 oy\n*Dars kunlari:* Seshanba, Payshanba, Shanba\n*Soat:* 18:00 - 20:00\n*Narxi:* 1 200 000 so‘m / oy\n\n⭐ Kurs yakunida sertifikat beriladi!",
#         "video": "excel_pro_max.mp4"
#     }
# }
#
# # Start tugmalari
# def start_buttons():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add("📚 Kurslarimiz", "👨‍🏫 Mutaxassislarimiz")
#     markup.add("ℹ️ Excel Masters haqida", "📞 Biz bilan bog‘lanish")
#     return markup
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, f"Assalamu alaykum hurmatli {message.from_user.first_name}!\n\n\
#     🎓 *Excel Masters* o'quv markazining rasmiy Telegram botiga xush kelibsiz!\n\n\
#     Siz bu yerda bizning kurslarimiz haqida batafsil ma'lumot olishingiz mumkin.", reply_markup=start_buttons())
#
# @bot.message_handler(func=lambda message: message.text == "📚 Kurslarimiz")
# def show_courses(message):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     for course in courses.keys():
#         markup.add(course)
#     markup.add("🔙 Orqaga")
#     bot.send_message(message.chat.id, "Quyidagi kurslardan birini tanlang:", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text in courses.keys())
# def course_info(message):
#     course = courses[message.text]
#     with open(course["video"], "rb") as video:
#         bot.send_video(message.chat.id, video)
#     bot.send_message(message.chat.id, course["info"], parse_mode="Markdown")
#
# @bot.message_handler(func=lambda message: message.text == "ℹ️ Excel Masters haqida")
# def about_excel_masters(message):
#     bot.send_message(message.chat.id, "🏫 *Excel Masters* haqida\n\n📅 2021-yilda tashkil topgan\n👨‍💼 *Asoschi:* Shahzod Sayfulla Begzod o‘g‘li\n🎓 3000+ muvaffaqiyatli bitiruvchilar\n💼 12 yillik MS Excel mutaxassisi (auditor)", parse_mode="Markdown")
#
# @bot.message_handler(func=lambda message: message.text == "👨‍🏫 Mutaxassislarimiz")
# def show_teachers(message):
#     bot.send_message(message.chat.id, "Bizning tajribali mutaxassislarimiz:\n\n👨‍🏫 *Shahzod Sayfulla* - MS Excel auditor\n👩‍🏫 *Dilnoza Akramova* - Excel va Power BI mutaxassisi\n👨‍🏫 *Jamshid Karimov* - Data Analyst", parse_mode="Markdown")
#
# @bot.message_handler(func=lambda message: message.text == "📞 Biz bilan bog‘lanish")
# def contact_info(message):
#     bot.send_message(message.chat.id, "📞 Aloqa ma’lumotlari:\n📱 Telefon: +998 90 123 45 67\n📨 Telegram: @ExcelMastersSupport", parse_mode="Markdown")
#
# @bot.message_handler(func=lambda message: message.text == "🔙 Orqaga")
# def back_to_start(message):
#     bot.send_message(message.chat.id, "Asosiy menyuga qaytdingiz.", reply_markup=start_buttons())
#
# bot.polling(none_stop=True)


# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
#
# TOKEN = "7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ"
# bot = telebot.TeleBot(TOKEN)
#
# # 🎛 Asosiy menyu
# def main_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("📖 Kurslarimiz"), KeyboardButton("👨‍🏫 Mutaxassislarimiz"))
#     markup.add(KeyboardButton("ℹ️ Excel Masters haqida"), KeyboardButton("📞 Biz bilan bog‘lanish"))
#     return markup
#
# # 📖 Kurslar menyusi
# def courses_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("🖥 Kompyuter Savodxonligi"), KeyboardButton("📊 Excel Boshlang‘ich"))
#     markup.add(KeyboardButton("📈 Excel Pro"), KeyboardButton("📉 Excel Pro Max"))
#     markup.add(KeyboardButton("🔙 Orqaga"))
#     return markup
#
# # 👨‍🏫 Mutaxassislar menyusi
# def teachers_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("👨‍🏫 Shoazim aka"), KeyboardButton("👨‍🏫 Feruzbek aka"))
#     markup.add(KeyboardButton("👨‍🏫 Begzod aka"))
#     markup.add(KeyboardButton("🔙 Orqaga"))
#     return markup
#
# # 📞 Aloqa menyusi
# def contact_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("📍 Bizning manzil"), KeyboardButton("🔙 Orqaga"))
#     return markup
#
# # 🏁 START komandasi
# @bot.message_handler(commands=['start'])
# def start(message):
#     text = f"Assalamu alaykum, hurmatli {message.from_user.first_name}! 👋\n\n" + \
#            "🎓 Excel Masters o‘quv markazining rasmiy Telegram botiga xush kelibsiz!\n\n" + \
#            "Siz bu yerda bizning kurslarimiz va mutaxassislarimiz haqida ma‘lumot olishingiz mumkin."
#     bot.send_message(message.chat.id, text, reply_markup=main_menu())
#
# # 📖 Kurslar
# @bot.message_handler(func=lambda message: message.text == "📖 Kurslarimiz")
# def courses(message):
#     text = "📚 Bizning kurslarimiz:\n\n" + \
#            "🖥 *Kompyuter Savodxonligi*\n📊 *Excel Boshlang‘ich*\n📈 *Excel Pro*\n📉 *Excel Pro Max*\n\n" + \
#            "Kerakli kursni tanlang."
#     bot.send_message(message.chat.id, text, reply_markup=courses_menu(), parse_mode="Markdown")
#
# # Kurslar haqida ma'lumotlar
# @bot.message_handler(func=lambda message: message.text in ["🖥 Kompyuter Savodxonligi", "📊 Excel Boshlang‘ich", "📈 Excel Pro", "📉 Excel Pro Max"])
# def course_info(message):
#     courses_info = {
#         "🖥 Kompyuter Savodxonligi": "🖥 *Kompyuter Savodxonligi* kursida siz kompyuter bilan ishlashning asoslarini o‘rganasiz.",
#         "📊 Excel Boshlang‘ich": "📊 *Excel Boshlang‘ich* kursida siz Excel dasturining boshlang‘ich darajalarini o‘rganasiz.",
#         "📈 Excel Pro": "📈 *Excel Pro* kursida murakkab Excel formulalari va avtomatlashtirish bo‘yicha bilim olasiz.",
#         "📉 Excel Pro Max": "📉 *Excel Pro Max* kursida professional darajadagi Excel imkoniyatlari o‘rgatiladi."
#     }
#     bot.send_message(message.chat.id, courses_info[message.text], reply_markup=courses_menu(), parse_mode="Markdown")
#
# # 👨‍🏫 Mutaxassislar
# @bot.message_handler(func=lambda message: message.text == "👨‍🏫 Mutaxassislarimiz")
# def teachers(message):
#     text = "👨‍🏫 *Bizning mutaxassislarimiz:*\n\n" + \
#            "👨‍🏫 *Shoazim aka* - 10 yillik tajribaga ega Excel bo‘yicha mutaxassis\n" + \
#            "👨‍🏫 *Feruzbek aka* - VBA va avtomatlashtirish bo‘yicha mutaxassis\n" + \
#            "👨‍🏫 *Begzod aka* - Excel va Google Sheets bo‘yicha tajribali o‘qituvchi\n\n" + \
#            "O‘qituvchini tanlang."
#     bot.send_message(message.chat.id, text, reply_markup=teachers_menu(), parse_mode="Markdown")
#
# # O‘qituvchilar haqida ma'lumot
# @bot.message_handler(func=lambda message: message.text in ["👨‍🏫 Shoazim aka", "👨‍🏫 Feruzbek aka", "👨‍🏫 Begzod aka"])
# def teacher_info(message):
#     teachers_info = {
#         "👨‍🏫 Shoazim aka": "👨‍🏫 *Shoazim aka*\n🧑‍🏫 10 yillik tajriba\n📚 Excel bo‘yicha mutaxassis\n📊 Kurslar: Excel Pro, Excel Pro Max",
#         "👨‍🏫 Feruzbek aka": "👨‍🏫 *Feruzbek aka*\n🔄 VBA va avtomatlashtirish bo‘yicha ekspert\n📈 Kurslar: Excel Pro, Excel avtomatlashtirish",
#         "👨‍🏫 Begzod aka": "👨‍🏫 *Begzod aka*\n📋 Google Sheets va Excel bo‘yicha tajribali o‘qituvchi\n📚 Kurslar: Excel boshlang‘ich, Excel Pro"
#     }
#     bot.send_message(message.chat.id, teachers_info[message.text], reply_markup=teachers_menu(), parse_mode="Markdown")
#
# # ℹ️ Excel Masters haqida
# @bot.message_handler(func=lambda message: message.text == "ℹ️ Excel Masters haqida")
# def about_excel_masters(message):
#     text = "ℹ️ *Excel Masters* - bu professional Excel mutaxassislari tomonidan tashkil etilgan o‘quv markazi.\n\n" + \
#            "🎓 Asoschi: *Shahzod Sayfulla Begzod o'g'li*\n📆 2021-yildan beri faoliyat yuritamiz.\n✅ 3000+ dan ortiq bitiruvchilar!"
#     bot.send_message(message.chat.id, text, reply_markup=main_menu(), parse_mode="Markdown")
#
# # 📞 Biz bilan bog‘lanish
# @bot.message_handler(func=lambda message: message.text == "📞 Biz bilan bog‘lanish")
# def contact(message):
#     text = "📞 *Qo‘shimcha savollaringiz yoki shikoyatlaringiz bo‘lsa, quyidagi ma'lumotlarga murojaat qiling:*\n\n" + \
#            "📲 *Telefon:* +998 90 968 61 61\n📩 *Telegram:* @excelmasters_Shoazim"
#     bot.send_message(message.chat.id, text, reply_markup=contact_menu(), parse_mode="Markdown")
#
# # 📍 Manzil
# @bot.message_handler(func=lambda message: message.text == "📍 Bizning manzil")
# def location(message):
#     text = "📍 *Excel Masters manzili:*\n🏢 Toshkent, Chilonzor tumani, Novza Metroni yaqinida joylashgan"
#     bot.send_message(message.chat.id, text, reply_markup=contact_menu(), parse_mode="Markdown")
#
# # 🔙 Orqaga qaytish
# @bot.message_handler(func=lambda message: message.text == "🔙 Orqaga")
# def back(message):
#     bot.send_message(message.chat.id, "🏠 Asosiy menyu", reply_markup=main_menu())
#
# bot.polling(none_stop=True)


# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
#
# bot = telebot.TeleBot('7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ')  # Tokeningizni shu yerga qo‘ying
#
#
# # 🏠 Asosiy menyu tugmalari
# def main_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(
#         KeyboardButton("📚 Mutaxassislarimiz"),
#         KeyboardButton("📖 Kurslarimiz")
#     )
#     markup.add(
#         KeyboardButton("ℹ️ Excel Masters haqida"),
#         KeyboardButton("📞 Biz bilan bog‘lanish")
#     )
#     return markup
#
#
# # 📖 Kurslar menyusi
# def courses_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("🖥 Kompyuter Savodxonligi"))
#     markup.add(KeyboardButton("📊 Excel Boshlang‘ich"))
#     markup.add(KeyboardButton("📈 Excel Pro"))
#     markup.add(KeyboardButton("📉 Excel Pro Max"))
#     markup.add(KeyboardButton("⬅️ Orqaga"))
#     return markup
#
#
# # 📚 Mutaxassislar menyusi
# def specialists_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("👨‍🏫 Shoazim"))
#     markup.add(KeyboardButton("👨‍🏫 Feruzbek"))
#     markup.add(KeyboardButton("👨‍🏫 Begzod"))
#     markup.add(KeyboardButton("⬅️ Orqaga"))
#     return markup
#
#
# # 📖 Kurslar haqida ma’lumot
# course_info = {
#     "🖥 Kompyuter Savodxonligi":
#         "✅ **🖥 Kompyuter Savodxonligi**\n"
#         "📌 Kompyuter bilan ishlashni endi boshlaganlar uchun asosiy kurs.\n"
#         "📌 Windows operatsion tizimi, fayllar bilan ishlash, internet xavfsizligi va asosiy ofis dasturlaridan foydalanishni o‘rgatadi.\n"
#         "📌 Microsoft Word va PowerPoint bilan ishlash ko‘nikmalari ham kiritilgan.",
#
#     "📊 Excel Boshlang‘ich":
#         "✅ **📊 Excel Boshlang‘ich**\n"
#         "📌 Excel'ning asosiy imkoniyatlari: jadval yaratish, formulalar, funksiyalar va diagrammalar bilan ishlash.\n"
#         "📌 Ma’lumotlarni saralash, filtrlash va asosiy hisob-kitoblarni bajarish usullari.\n"
#         "📌 Ish jarayonini tezlashtirish uchun muhim Excel qisqayollari.",
#
#     "📈 Excel Pro":
#         "✅ **📈 Excel Pro**\n"
#         "📌 Murakkab Excel formulalari (VLOOKUP, INDEX-MATCH, IF va boshqalar) bilan ishlash.\n"
#         "📌 Dinamik jadval va avtomatik hisobotlar yaratish.\n"
#         "📌 Excel’da katta hajmdagi ma’lumotlarni tahlil qilish va vizualizatsiya qilish.",
#
#     "📉 Excel Pro Max":
#         "✅ **📉 Excel Pro Max**\n"
#         "📌 VBA (Visual Basic for Applications) dasturlash orqali Excel’ni avtomatlashtirish.\n"
#         "📌 Makroslar yozish, murakkab hisobot va tahliliy vositalar yaratish.\n"
#         "📌 Korporativ darajadagi Excel ish usullari va Data Analysis (ma’lumotlarni tahlil qilish) texnikalarini o‘rgatish."
# }
#
# # 📚 Mutaxassislar haqida ma’lumot
# specialist_info = {
#     "👨‍🏫 Shoazim":
#         "👨‍🏫 **Shoazim**\n"
#         "📌 Tajribasi: 7 yil\n"
#         "📌 Yo‘nalishi: Excel va Data Analysis\n"
#         "📌 Dars beradigan kurslar: 📈 Excel Pro, 📉 Excel Pro Max",
#
#     "👨‍🏫 Feruzbek":
#         "👨‍🏫 **Feruzbek**\n"
#         "📌 Tajribasi: 5 yil\n"
#         "📌 Yo‘nalishi: Boshlang‘ich Excel va Kompyuter savodxonligi\n"
#         "📌 Dars beradigan kurslar: 📊 Excel Boshlang‘ich, 🖥 Kompyuter Savodxonligi",
#
#     "👨‍🏫 Begzod":
#         "👨‍🏫 **Begzod**\n"
#         "📌 Tajribasi: 6 yil\n"
#         "📌 Yo‘nalishi: Excel va Biznes Analytics\n"
#         "📌 Dars beradigan kurslar: 📈 Excel Pro, 📉 Excel Pro Max"
# }
#
# # 📞 Bog‘lanish ma’lumotlari
# contact_info = (
#     "📞 **Biz bilan bog‘lanish:**\n"
#     "📌 Qo‘shimcha savollaringiz yoki shikoyatlaringiz bo‘lsa, quyidagi manzillarga murojaat qiling:\n"
#     "📩 Telegram: @contact_username\n"
#     "📍 **Bizning manzil:** [Google Maps](https://goo.gl/maps/example)"
# )
#
#
# # 📩 Xabarlarni qayta ishlash
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, "👋 Assalomu alaykum! Excel Masters botiga xush kelibsiz!",
#                      reply_markup=main_menu())
#
#
# @bot.message_handler(func=lambda message: message.text in ["📖 Kurslarimiz", "⬅️ Orqaga"])
# def send_courses(message):
#     bot.send_message(message.chat.id, "📖 Kurslarimiz ro‘yxati:", reply_markup=courses_menu())
#
#
# @bot.message_handler(func=lambda message: message.text in course_info.keys())
# def send_course_info(message):
#     bot.send_message(message.chat.id, course_info[message.text], parse_mode="Markdown", reply_markup=courses_menu())
#
#
# @bot.message_handler(func=lambda message: message.text in ["📚 Mutaxassislarimiz", "⬅️ Orqaga"])
# def send_specialists(message):
#     bot.send_message(message.chat.id, "📚 Bizning mutaxassislar:", reply_markup=specialists_menu())
#
#
# @bot.message_handler(func=lambda message: message.text in specialist_info.keys())
# def send_specialist_info(message):
#     bot.send_message(message.chat.id, specialist_info[message.text], parse_mode="Markdown",
#                      reply_markup=specialists_menu())
#
#
# @bot.message_handler(func=lambda message: message.text == "ℹ️ Excel Masters haqida")
# def send_excel_masters_info(message):
#     bot.send_message(message.chat.id,
#                      "ℹ️ Excel Masters - bu yuqori darajadagi Excel va Data Analysis kurslarini taqdim etuvchi platforma. Bu yerda tajribali ustozlar bilan professional darajada bilim olish imkoniyati mavjud.",
#                      reply_markup=main_menu())
#
#
# @bot.message_handler(func=lambda message: message.text == "📞 Biz bilan bog‘lanish")
# def send_contact_info(message):
#     contact_info = (
#         "📞 *Biz bilan bog‘lanish:*\n"
#         "📌 Qo‘shimcha savollaringiz yoki shikoyatlaringiz bo‘lsa, quyidagi manzillarga murojaat qiling:\n"
#         "📩 Telegram: @contact_username\n"
#         "📍 *Bizning manzil:* [Google Maps](https://goo.gl/maps/example)"
#     )
#
#     bot.send_message(message.chat.id, contact_info, parse_mode="Markdown", disable_web_page_preview=True)
#
#
# # 🤖 Botni ishga tushirish
# bot.polling(none_stop=True)



# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
#
# bot = telebot.TeleBot('7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ')  # Tokeningizni shu yerga qo‘ying
#
# # 🏠 Asosiy menyu tugmalari
# def main_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(
#         KeyboardButton("📚 Mutaxassislarimiz"),
#         KeyboardButton("📖 Kurslarimiz")
#     )
#     markup.add(
#         KeyboardButton("ℹ️ Excel Masters haqida"),
#         KeyboardButton("📞 Biz bilan bog‘lanish")
#     )
#     return markup
#
# # 📖 Kurslar menyusi
# def courses_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("🖥 Kompyuter Savodxonligi"))
#     markup.add(KeyboardButton("📊 Excel Boshlang‘ich"))
#     markup.add(KeyboardButton("📈 Excel Pro"))
#     markup.add(KeyboardButton("📉 Excel Pro Max"))
#     markup.add(KeyboardButton("⬅️ Orqaga"))
#     return markup
#
# # 📚 Mutaxassislar menyusi
# def specialists_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("👨‍🏫 Shoazim"))
#     markup.add(KeyboardButton("👨‍🏫 Feruzbek"))
#     markup.add(KeyboardButton("👨‍🏫 Begzod"))
#     markup.add(KeyboardButton("⬅️ Orqaga"))
#     return markup
#
# # 📞 Bog‘lanish menyusi
# def contact_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("⬅️ Orqaga"))
#     return markup
#
# # 📖 Kurslar haqida ma’lumot
# course_info = {
#     "🖥 Kompyuter Savodxonligi": "✅ *Kompyuter Savodxonligi* kursi haqida ma’lumot.",
#     "📊 Excel Boshlang‘ich": "✅ *Excel Boshlang‘ich* kursi haqida ma’lumot.",
#     "📈 Excel Pro": "✅ *Excel Pro* kursi haqida ma’lumot.",
#     "📉 Excel Pro Max": "✅ *Excel Pro Max* kursi haqida ma’lumot."
# }
#
# # 📚 Mutaxassislar haqida ma’lumot
# specialist_info = {
#     "👨‍🏫 Shoazim": "👨‍🏫 *Shoazim* \n📌 Tajribasi: 7 yil\n📌 Yo‘nalishi: Excel va Data Analysis\n📌 Dars beradigan kurslar: 📈 Excel Pro, 📉 Excel Pro Max\n📌 O‘quvchilari: 500+",
#     "👨‍🏫 Feruzbek": "👨‍🏫 *Feruzbek* \n📌 Tajribasi: 5 yil\n📌 Yo‘nalishi: Boshlang‘ich Excel va Kompyuter savodxonligi\n📌 Dars beradigan kurslar: 📊 Excel Boshlang‘ich, 🖥 Kompyuter Savodxonligi\n📌 O‘quvchilari: 300+",
#     "👨‍🏫 Begzod": "👨‍🏫 *Begzod* \n📌 Tajribasi: 6 yil\n📌 Yo‘nalishi: Excel va Biznes Analytics\n📌 Dars beradigan kurslar: 📈 Excel Pro, 📉 Excel Pro Max\n📌 O‘quvchilari: 450+"
# }
#
# # 📞 Bog‘lanish ma’lumotlari
# def contact_info():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("📞 Telefon raqam", url="tel:+998901234567"))
#     markup.add(InlineKeyboardButton("📩 Telegram", url="https://t.me/contact_username"))
#     markup.add(InlineKeyboardButton("📍 Manzil (Google Maps)", url="https://goo.gl/maps/example"))
#     return markup
#
# # 📩 Xabarlarni qayta ishlash
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, "👋 Assalomu alaykum!", reply_markup=main_menu())
#
# @bot.message_handler(func=lambda message: message.text == "📖 Kurslarimiz")
# def send_courses(message):
#     bot.send_message(message.chat.id, "📖 Kurslarimiz ro‘yxati:", reply_markup=courses_menu())
#
# @bot.message_handler(func=lambda message: message.text in course_info.keys())
# def send_course_info(message):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("⬅️ Orqaga"))  # Har bir kurs ichida "⬅️ Orqaga" tugmasi
#     bot.send_message(message.chat.id, course_info[message.text], parse_mode="Markdown", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text == "📚 Mutaxassislarimiz")
# def send_specialists(message):
#     bot.send_message(message.chat.id, "📚 Bizning mutaxassislar:", reply_markup=specialists_menu())
#
# @bot.message_handler(func=lambda message: message.text in specialist_info.keys())
# def send_specialist_info(message):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("⬅️ Orqaga"))  # Har bir mutaxassis ichida "⬅️ Orqaga" tugmasi
#     bot.send_message(message.chat.id, specialist_info[message.text], parse_mode="Markdown", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text == "ℹ️ Excel Masters haqida")
# def send_excel_masters_info(message):
#     bot.send_message(message.chat.id, "ℹ️ Excel Masters haqida ma’lumot.", reply_markup=main_menu())
#
# @bot.message_handler(func=lambda message: message.text == "📞 Biz bilan bog‘lanish")
# def send_contact_info(message):
#     bot.send_message(message.chat.id, "📞 *Biz bilan bog‘lanish ma’lumotlari:*", parse_mode="Markdown", reply_markup=contact_info())
#
# # 🔙 Orqaga tugmasi
# @bot.message_handler(func=lambda message: message.text == "⬅️ Orqaga")
# def go_back(message):
#     bot.send_message(message.chat.id, "🏠 Asosiy menyuga qaytdingiz.", reply_markup=main_menu())
#
# # 🤖 Botni ishga tushirish
# bot.polling(none_stop=True)

# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
#
# bot = telebot.TeleBot('7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ')  # Tokeningizni shu yerga qo‘ying
#
# # 🏠 Asosiy menyu tugmalari
# def main_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(
#         KeyboardButton("📚 Mutaxassislarimiz"),
#         KeyboardButton("📖 Kurslarimiz")
#     )
#     markup.add(
#         KeyboardButton("ℹ️ Excel Masters haqida"),
#         KeyboardButton("📞 Biz bilan bog‘lanish")
#     )
#     return markup
#
# # 📖 Kurslar menyusi
# def courses_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("🖥 Kompyuter Savodxonligi"))
#     markup.add(KeyboardButton("📊 Excel Boshlang‘ich"))
#     markup.add(KeyboardButton("📈 Excel Pro"))
#     markup.add(KeyboardButton("📉 Excel Pro Max"))
#     markup.add(KeyboardButton("⬅️ Asosiy menyu"))
#     return markup
#
# # 📚 Mutaxassislar menyusi
# def specialists_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("👨‍🏫 Shoazim"))
#     markup.add(KeyboardButton("👨‍🏫 Feruzbek"))
#     markup.add(KeyboardButton("👨‍🏫 Begzod"))
#     markup.add(KeyboardButton("⬅️ Asosiy menyu"))
#     return markup
#
# # 📖 Kurslar haqida batafsil ma’lumot
# course_info = {
#     "🖥 Kompyuter Savodxonligi": "✅ **🖥 Kompyuter Savodxonligi**\n📌 Asosiy kompyuter bilimlarini o‘rgatuvchi kurs.",
#     "📊 Excel Boshlang‘ich": "✅ **📊 Excel Boshlang‘ich**\n📌 Excel bilan ishlashni boshlash uchun eng yaxshi kurs.",
#     "📈 Excel Pro": "✅ **📈 Excel Pro**\n📌 Murakkab Excel funksiyalari va formulalari bilan ishlashni o‘rgatadi.",
#     "📉 Excel Pro Max": "✅ **📉 Excel Pro Max**\n📌 Excel avtomatlashtirish va VBA dasturlashni o‘rgatish kursi."
# }
#
# # 📚 Mutaxassislar haqida ma’lumot
# specialist_info = {
#     "👨‍🏫 Shoazim": "👨‍🏫 **Shoazim**\n📌 Excel va Data Analysis bo‘yicha 7 yillik tajribaga ega instruktor.",
#     "👨‍🏫 Feruzbek": "👨‍🏫 **Feruzbek**\n📌 Excel va Kompyuter savodxonligi bo‘yicha 5 yillik tajribaga ega instruktor.",
#     "👨‍🏫 Begzod": "👨‍🏫 **Begzod**\n📌 Excel va Biznes Analytics bo‘yicha 6 yillik tajribaga ega instruktor."
# }
#
# # ℹ️ Excel Masters haqida
# excel_masters_info = (
#     "ℹ️ **Excel Masters** – bu tajribali mutaxassislar tomonidan o‘qitiladigan **Excel va Data Analysis** bo‘yicha professional kurslar markazi.\n"
#     "📌 Bizning kurslarimiz orqali siz quyidagilarni o‘rganasiz:\n"
#     "✅ Excel’da ma’lumotlar bilan samarali ishlash\n"
#     "✅ Murakkab formulalar va avtomatik hisobotlar yaratish\n"
#     "✅ VBA yordamida jarayonlarni avtomatlashtirish\n"
#     "✅ Ma’lumotlar tahlili va vizualizatsiyasi\n\n"
#     "📍 Kurslar oflayn va onlayn tarzda o‘tkaziladi."
# )
#
# # 📞 Bog‘lanish ma’lumotlari
# contact_info_text = (
#     "📞 **Biz bilan bog‘lanish:**\n"
#     "📲 Telefon: +998901234567\n"
#     "✉️ Telegram: @contact_username\n"
#     "📍 Manzil: Toshkent, Mustaqillik shoh ko‘chasi, 10-uy"
# )
#
# # 📩 Xabarlarni qayta ishlash
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, "👋 Assalomu alaykum! Excel Masters botiga xush kelibsiz!", reply_markup=main_menu())
#
# @bot.message_handler(func=lambda message: message.text == "📖 Kurslarimiz")
# def send_courses(message):
#     bot.send_message(message.chat.id, "📖 Kurslarimiz ro‘yxati:", reply_markup=courses_menu())
#
# @bot.message_handler(func=lambda message: message.text in course_info.keys())
# def send_course_info(message):
#     bot.send_message(message.chat.id, course_info[message.text], parse_mode="Markdown", reply_markup=courses_menu())
#
# @bot.message_handler(func=lambda message: message.text == "📚 Mutaxassislarimiz")
# def send_specialists(message):
#     bot.send_message(message.chat.id, "📚 Bizning mutaxassislar:", reply_markup=specialists_menu())
#
# @bot.message_handler(func=lambda message: message.text in specialist_info.keys())
# def send_specialist_info(message):
#     bot.send_message(message.chat.id, specialist_info[message.text], parse_mode="Markdown", reply_markup=specialists_menu())
#
# @bot.message_handler(func=lambda message: message.text == "ℹ️ Excel Masters haqida")
# def send_excel_masters_info(message):
#     bot.send_message(message.chat.id, excel_masters_info, parse_mode="Markdown", reply_markup=main_menu())
#
# @bot.message_handler(func=lambda message: message.text == "📞 Biz bilan bog‘lanish")
# def send_contact_info(message):
#     bot.send_message(message.chat.id, contact_info_text, parse_mode="Markdown", reply_markup=main_menu())
#
# # 🔄 Orqaga qaytish tugmalarini to‘g‘ri ishlashini ta’minlash
# @bot.message_handler(func=lambda message: message.text == "⬅️ Asosiy menyu")
# def go_main_menu(message):
#     bot.send_message(message.chat.id, "🏠 Asosiy menyuga qaytdingiz.", reply_markup=main_menu())
#
# # 🤖 Botni ishga tushirish
# bot.polling(none_stop=True)


# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
#
# bot = telebot.TeleBot('7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ')  # Tokeningizni shu yerga qo‘ying
#
#
# # 🏠 Asosiy menyu
# def main_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(
#         KeyboardButton("📚 Mutaxassislarimiz"),
#         KeyboardButton("📖 Kurslarimiz")
#     )
#     markup.add(
#         KeyboardButton("ℹ️ Excel Masters haqida"),
#         KeyboardButton("📞 Biz bilan bog‘lanish")
#     )
#     return markup
#
#
# # 📖 Kurslar menyusi
# def courses_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("🖥 Kompyuter Savodxonligi"))
#     markup.add(KeyboardButton("📊 Excel Boshlang‘ich"))
#     markup.add(KeyboardButton("📈 Excel Pro"))
#     markup.add(KeyboardButton("📉 Excel Pro Max"))
#     markup.add(KeyboardButton("⬅️ Asosiy menyu"))
#     return markup
#
#
# # 📚 Mutaxassislar menyusi
# def specialists_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("👨‍🏫 Shoazim"))
#     markup.add(KeyboardButton("👨‍🏫 Feruzbek"))
#     markup.add(KeyboardButton("👨‍🏫 Begzod"))
#     markup.add(KeyboardButton("⬅️ Asosiy menyu"))
#     return markup
#
#
# # 📖 Kurslar haqida batafsil ma’lumot
# course_info = {
#     "🖥 Kompyuter Savodxonligi":
#         "✅ **🖥 Kompyuter Savodxonligi**\n"
#         "📌 Word va PowerPoint dasturlaridan foydalanish\n"
#         "📌 Internet va e-mail bilan ishlash asoslari\n"
#         "📌 Windows operatsion tizimi va fayl boshqaruvi\n"
#         "📅 Kurs boshlanishi: 1-aprel 2025\n"
#         "⏳ Muddati: 2 oy\n"
#         "💰 Narxi: 500 000 so‘m/oyiga\n"
#         "📋 Har bir kursni oxirida siz Sertifikat bilan taqdirlanasiz!\n",
#
#     "📊 Excel Boshlang‘ich":
#         "✅ **📊 Excel Boshlang‘ich**\n"
#         "📌 Jadval yaratish va hujayralar bilan ishlash\n"
#         "📌 Asosiy formulalar va funksiyalar\n"
#         "📌 Diagrammalar va shartli formatlash\n"
#         "📅 Kurs boshlanishi: 10-aprel 2025\n"
#         "⏳ Muddati: 2,5 oy\n"
#         "💰 Narxi: 600 000 so‘m/oyiga\n"
#         "📋 Har bir kursni oxirida siz Sertifikat bilan taqdirlanasiz!\n",
#
#     "📈 Excel Pro":
#         "✅ **📈 Excel Pro**\n"
#         "📌 Murakkab funksiyalar va formulalar\n"
#         "📌 Ma'lumotlarni filtrlash va saralash\n"
#         "📌 Pivot jadval va avtomatlashtirish\n"
#         "📅 Kurs boshlanishi: 20-aprel 2025\n"
#         "⏳ Muddati: 3 oy\n"
#         "💰 Narxi: 750 000 so‘m/oyiga\n"
#         "📋 Har bir kursni oxirida siz Sertifikat bilan taqdirlanasiz!\n",
#
#     "📉 Excel Pro Max":
#         "✅ **📉 Excel Pro Max**\n"
#         "📌 VBA (Visual Basic for Applications) dasturlash\n"
#         "📌 Katta ma'lumotlar bilan ishlash\n"
#         "📌 Ish jarayonlarini avtomatlashtirish\n"
#
#         "📅 Kurs boshlanishi: 5-may 2025\n"
#         "⏳ Muddati: 4 oy\n"
#         "💰 Narxi: 900 000 so‘m/oyiga\n"
#         "📋 Har bir kursni oxirida siz Sertifikat bilan taqdirlanasiz!\n",
# }
#
# # 📚 Mutaxassislar haqida batafsil ma’lumot
# specialist_info = {
#     "👨‍🏫 Shoazim":
#         "👨‍🏫 **Shoazim**\n"
#         "📌 7 yillik tajribaga ega, Data Analyst.\n"
#         "📚 Mutaxassisligi: Excel, Power BI, SQL\n"
#         "🎓 Microsoft sertifikatiga ega.",
#
#     "👨‍🏫 Feruzbek":
#         "👨‍🏫 **Feruzbek**\n"
#         "📌 5 yillik tajribaga ega, Excel treneri.\n"
#         "📚 Mutaxassisligi: Excel, Google Sheets\n"
#         "🎓 Excel bo‘yicha xalqaro sertifikatga ega.",
#
#     "👨‍🏫 Begzod":
#         "👨‍🏫 **Begzod**\n"
#         "📌 6 yillik tajribaga ega, biznes analitik.\n"
#         "📚 Mutaxassisligi: Excel, Python, Power Query\n"
#         "🎓 Data Science bo‘yicha tajribaga ega."
# }
#
# # ℹ️ Excel Masters haqida
# excel_masters_info = (
#     "ℹ️ **Excel Masters** – bu tajribali mutaxassislar tomonidan o‘qitiladigan **Excel va Data Analysis** bo‘yicha professional kurslar markazi.\n"
#     "📍 **Tashkil etilgan yil**: 2021\n"
#     "👨‍💼 **Asoschisi**: Shahzod Sayfulla Begzod o'g'li\n"
#     "‍💻Microsoft Companiyasi Partneri\n"
#     "📊 12 yillik MS Excel Mutaxassisi (auditor)\n"
#     "🏆3000+ Muvaffaqiyatli o’quvchilar\n"
#     "📌 Bizning kurslarimiz orqali siz quyidagilarni o‘rganasiz:\n"
#     "✅ Excel’da ma’lumotlar bilan samarali ishlash\n"
#     "✅ Murakkab formulalar va avtomatik hisobotlar yaratish\n"
#     "✅ VBA yordamida jarayonlarni avtomatlashtirish\n"
#     "✅ Ma’lumotlar tahlili va vizualizatsiyasi\n\n"
#     "📍 Kurslar oflayn va onlayn tarzda o‘tkaziladi."
# )
#
# # 📞 Bog‘lanish ma’lumotlari (xato to‘g‘rilandi)
# contact_info_text = (
#     "📞 **Biz bilan bog‘lanish:**\n\n"
#     "📲 **Telefon:** +998 90 968 61 61\n"
#     "✉️ **Telegram:** [@excelmasters_Shoazim](https://t.me/excelmasters_Shoazim)\n"
#     "📍 **Manzil:** Toshkent, Chilonzor Tumani, Novza Metroni yonginasida "
# )
#
# @bot.message_handler(func=lambda message: message.text == "📞 Biz bilan bog‘lanish")
# def send_contact_info(message):
#     bot.send_message(message.chat.id, contact_info_text, parse_mode="Markdown", reply_markup=main_menu())
#
#
#
# # 📩 Xabarlarni qayta ishlash
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f"Assalomu alaykum, {message.from_user.first_name} 👋 ! \nExcel Masters va bizning kurslarimiz haqida ma’lumot olish uchun quyidagi menyudan tanlang:",
#                      reply_markup=main_menu())
#
#
# @bot.message_handler(func=lambda message: message.text == "📖 Kurslarimiz")
# def send_courses(message):
#     bot.send_message(message.chat.id, "📖 Kurslarimiz ro‘yxati:", reply_markup=courses_menu())
#
#
# @bot.message_handler(func=lambda message: message.text in course_info.keys())
# def send_course_info(message):
#     bot.send_message(message.chat.id, course_info[message.text], parse_mode="Markdown", reply_markup=courses_menu())
#
#
# @bot.message_handler(func=lambda message: message.text == "📚 Mutaxassislarimiz")
# def send_specialists(message):
#     bot.send_message(message.chat.id, "📚 Bizning mutaxassislar:", reply_markup=specialists_menu())
#
#
# @bot.message_handler(func=lambda message: message.text in specialist_info.keys())
# def send_specialist_info(message):
#     bot.send_message(message.chat.id, specialist_info[message.text], parse_mode="Markdown",
#                      reply_markup=specialists_menu())
#
#
# @bot.message_handler(func=lambda message: message.text == "ℹ️ Excel Masters haqida")
# def send_excel_masters_info(message):
#     bot.send_message(message.chat.id, excel_masters_info, parse_mode="Markdown", reply_markup=main_menu())
#
#
# @bot.message_handler(func=lambda message: message.text == "📞 Biz bilan bog‘lanish")
# def send_contact_info(message):
#     bot.send_message(message.chat.id, contact_info_text, parse_mode="Markdown", reply_markup=main_menu())
#
#
# @bot.message_handler(func=lambda message: message.text == "⬅️ Asosiy menyu")
# def go_main_menu(message):
#     bot.send_message(message.chat.id, "🏠 Asosiy menyuga qaytdingiz.", reply_markup=main_menu())
#
#
# bot.polling(none_stop=True)


# import telebot
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# bot = telebot.TeleBot("7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ")  # Tokeningizni shu yerga qo‘ying
#
# # 📖 Kurslar haqida ma’lumotlar
# course_info = {
#     "🖥 Kompyuter Savodxonligi":
#         "✅ **🖥 Kompyuter Savodxonligi**\n"
#         "📌 Word va PowerPoint dasturlaridan foydalanish\n"
#         "📌 Internet va e-mail bilan ishlash asoslari\n"
#         "📌 Windows operatsion tizimi va fayl boshqaruvi\n"
#         "📅 Kurs boshlanishi: 1-aprel 2025\n"
#         "⏳ Muddati: 2 oy\n"
#         "💰 Narxi: 500 000 so‘m/oyiga\n"
#         "📋 Sertifikat beriladi!\n",
#
#     "📊 Excel Boshlang‘ich":
#         "✅ **📊 Excel Boshlang‘ich**\n"
#         "📌 Jadval yaratish va hujayralar bilan ishlash\n"
#         "📌 Asosiy formulalar va funksiyalar\n"
#         "📌 Diagrammalar va shartli formatlash\n"
#         "📅 Kurs boshlanishi: 10-aprel 2025\n"
#         "⏳ Muddati: 2,5 oy\n"
#         "💰 Narxi: 600 000 so‘m/oyiga\n"
#         "📋 Sertifikat beriladi!\n"
# }
#
# # 📚 Mutaxassislar haqida ma’lumot
# specialist_info = {
#     "👨‍🏫 Shoazim":
#         "👨‍🏫 **Shoazim**\n"
#         "📌 7 yillik tajribaga ega, Data Analyst.\n"
#         "📚 Mutaxassisligi: Excel, Power BI, SQL\n"
#         "🎓 Microsoft sertifikatiga ega.",
#
#     "👨‍🏫 Feruzbek":
#         "👨‍🏫 **Feruzbek**\n"
#         "📌 5 yillik tajribaga ega, Excel treneri.\n"
#         "📚 Mutaxassisligi: Excel, Google Sheets\n"
#         "🎓 Excel bo‘yicha xalqaro sertifikatga ega."
# }
#
#
# # 🏠 Asosiy menyu
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     text = f"Assalomu alaykum, {message.from_user.first_name} 👋 ! \nExcel Masters va bizning kurslarimiz haqida ma’lumot olish uchun quyidagi menyudan tanlang:"
#
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("📚 Mutaxassislarimiz", callback_data="specialists"))
#     markup.add(InlineKeyboardButton("📖 Kurslarimiz", callback_data="courses"))
#     markup.add(InlineKeyboardButton("ℹ️ Excel Masters haqida", callback_data="about"))
#     markup.add(InlineKeyboardButton("📞 Biz bilan bog‘lanish", callback_data="contact"))
#
#     bot.send_message(message.chat.id, text, reply_markup=markup)
#
#
# # 📖 Kurslar menyusi
# @bot.callback_query_handler(func=lambda call: call.data == "courses")
# def courses_menu(call):
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("🖥 Kompyuter Savodxonligi", callback_data="course_1"))
#     markup.add(InlineKeyboardButton("📊 Excel Boshlang‘ich", callback_data="course_2"))
#     markup.add(InlineKeyboardButton("⬅️ Asosiy menyu", callback_data="main_menu"))
#
#     bot.edit_message_text("📖 Kurslarimiz ro‘yxati:", call.message.chat.id, call.message.message_id, reply_markup=markup)
#
#
# # 📚 Mutaxassislar menyusi
# @bot.callback_query_handler(func=lambda call: call.data == "specialists")
# def specialists_menu(call):
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("👨‍🏫 Shoazim", callback_data="specialist_1"))
#     markup.add(InlineKeyboardButton("👨‍🏫 Feruzbek", callback_data="specialist_2"))
#     markup.add(InlineKeyboardButton("⬅️ Asosiy menyu", callback_data="main_menu"))
#
#     bot.edit_message_text("📚 Bizning mutaxassislar:", call.message.chat.id, call.message.message_id,
#                           reply_markup=markup)
#
#
# # 📖 Kurslar haqida batafsil ma’lumot
# @bot.callback_query_handler(func=lambda call: call.data.startswith("course_"))
# def send_course_info(call):
#     course_keys = list(course_info.keys())
#     course_index = int(call.data.split("_")[1]) - 1
#     text = course_info[course_keys[course_index]]
#
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("⬅️ Kurslar menyusi", callback_data="courses"))
#
#     bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode="Markdown",
#                           reply_markup=markup)
#
#
# # 📚 Mutaxassislar haqida batafsil ma’lumot
# @bot.callback_query_handler(func=lambda call: call.data.startswith("specialist_"))
# def send_specialist_info(call):
#     specialist_keys = list(specialist_info.keys())
#     specialist_index = int(call.data.split("_")[1]) - 1
#     text = specialist_info[specialist_keys[specialist_index]]
#
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("⬅️ Mutaxassislar menyusi", callback_data="specialists"))
#
#     bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode="Markdown",
#                           reply_markup=markup)
#
#
# # ℹ️ Excel Masters haqida
# @bot.callback_query_handler(func=lambda call: call.data == "about")
# def send_excel_masters_info(call):
#     text = (
#         "ℹ️ **Excel Masters** – bu tajribali mutaxassislar tomonidan o‘qitiladigan **Excel va Data Analysis** bo‘yicha professional kurslar markazi.\n"
#         "📍 **Tashkil etilgan yil**: 2021\n"
#         "👨‍💼 **Asoschisi**: Shahzod Sayfulla Begzod o'g'li\n"
#         "‍💻Microsoft Companiyasi Partneri\n"
#         "📊 12 yillik MS Excel Mutaxassisi (auditor)\n"
#         "🏆3000+ Muvaffaqiyatli o’quvchilar\n"
#     )
#
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("⬅️ Asosiy menyu", callback_data="main_menu"))
#
#     bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode="Markdown",
#                           reply_markup=markup)
#
#
# # 📞 Biz bilan bog‘lanish
# @bot.callback_query_handler(func=lambda call: call.data == "contact")
# def send_contact_info(call):
#     text = (
#         "📞 **Biz bilan bog‘lanish:**\n\n"
#         "📲 **Telefon:** +998 90 968 61 61\n"
#         "✉️ **Telegram:** [@excelmasters_Shoazim](https://t.me/excelmasters_Shoazim)\n"
#         "📍 **Manzil:** Toshkent, Chilonzor Tumani, Novza Metroni yonginasida"
#     )
#
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("⬅️ Asosiy menyu", callback_data="main_menu"))
#
#     bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode="Markdown",
#                           reply_markup=markup)
#
#
# # 🏠 Asosiy menyuga qaytish
# @bot.callback_query_handler(func=lambda call: call.data == "main_menu")
# def go_main_menu(call):
#     send_welcome(call.message)
#
#
# bot.polling(none_stop=True)

# import telebot
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# bot = telebot.TeleBot('7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ')  # Tokeningizni shu yerga qo‘ying
#
# # 🏠 Asosiy menyu
# def main_menu():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("📚 Mutaxassislarimiz", callback_data="specialists"))
#     markup.add(InlineKeyboardButton("📖 Kurslarimiz", callback_data="courses"))
#     markup.add(InlineKeyboardButton("ℹ️ Excel Masters haqida", callback_data="about"))
#     markup.add(InlineKeyboardButton("📞 Biz bilan bog‘lanish", callback_data="contact"))
#     return markup
#
# # 📖 Kurslar menyusi
# def courses_menu():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("🖥 Kompyuter Savodxonligi", callback_data="course_1"))
#     markup.add(InlineKeyboardButton("📊 Excel Boshlang‘ich", callback_data="course_2"))
#     markup.add(InlineKeyboardButton("📈 Excel Pro", callback_data="course_3"))
#     markup.add(InlineKeyboardButton("📉 Excel Pro Max", callback_data="course_4"))
#     markup.add(InlineKeyboardButton("⬅️ Asosiy menyu", callback_data="main_menu"))
#     return markup
#
# # 📚 Mutaxassislar menyusi
# def specialists_menu():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("👨‍🏫 Shoazim", callback_data="specialist_1"))
#     markup.add(InlineKeyboardButton("👨‍🏫 Feruzbek", callback_data="specialist_2"))
#     markup.add(InlineKeyboardButton("👨‍🏫 Begzod", callback_data="specialist_3"))
#     markup.add(InlineKeyboardButton("⬅️ Asosiy menyu", callback_data="main_menu"))
#     return markup
#
# # 📖 Kurslar haqida ma’lumot
# course_info = {
#     "course_1": "✅ **🖥 Kompyuter Savodxonligi**\n📌 Word, PowerPoint, Internet va fayl boshqaruvi\n📅 1-aprel 2025 | ⏳ 2 oy\n💰 500 000 so‘m/oyiga\n📋 Sertifikat beriladi!",
#     "course_2": "✅ **📊 Excel Boshlang‘ich**\n📌 Jadval yaratish, asosiy formulalar, diagrammalar\n📅 10-aprel 2025 | ⏳ 2,5 oy\n💰 600 000 so‘m/oyiga\n📋 Sertifikat beriladi!",
#     "course_3": "✅ **📈 Excel Pro**\n📌 Murakkab formulalar, Pivot jadval, avtomatlashtirish\n📅 20-aprel 2025 | ⏳ 3 oy\n💰 750 000 so‘m/oyiga\n📋 Sertifikat beriladi!",
#     "course_4": "✅ **📉 Excel Pro Max**\n📌 VBA, katta ma’lumotlar, avtomatlashtirish\n📅 5-may 2025 | ⏳ 4 oy\n💰 900 000 so‘m/oyiga\n📋 Sertifikat beriladi!"
# }
#
# # 📚 Mutaxassislar haqida ma’lumot
# specialist_info = {
#     "specialist_1": "👨‍🏫 **Shoazim**\n📌 7 yillik tajriba, Data Analyst\n📚 Excel, Power BI, SQL\n🎓 Microsoft sertifikati.",
#     "specialist_2": "👨‍🏫 **Feruzbek**\n📌 5 yillik tajriba, Excel treneri\n📚 Excel, Google Sheets\n🎓 Xalqaro sertifikat.",
#     "specialist_3": "👨‍🏫 **Begzod**\n📌 6 yillik tajriba, biznes analitik\n📚 Excel, Python, Power Query\n🎓 Data Science mutaxassisi."
# }
#
# # ℹ️ Excel Masters haqida
# excel_masters_info = "ℹ️ **Excel Masters** – Excel va Data Analysis bo‘yicha professional kurslar markazi.\n📌 Asosiy yo‘nalishlar: Excel, VBA, Power BI\n📍 Kurslar: onlayn va oflayn."
#
# # 📞 Bog‘lanish
# contact_info_text = "📞 **Biz bilan bog‘lanish:**\n📲 Telefon: +998 90 968 61 61\n✉️ Telegram: [@excelmasters_Shoazim](https://t.me/excelmasters_Shoazim)\n📍 Manzil: Toshkent, Chilonzor, Novza metrosi yonida."
#
# # 📩 Xabarlarni qayta ishlash
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f"Assalomu alaykum, {message.from_user.first_name} 👋 !\nExcel Masters kurslari haqida ma’lumot olish uchun quyidagi menyudan tanlang:", reply_markup=main_menu())
#
# # Callback handler
# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     if call.data == "main_menu":
#         bot.edit_message_text("🏠 Asosiy menyu:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
#
#     elif call.data == "courses":
#         bot.edit_message_text("📖 Kurslarimiz:", call.message.chat.id, call.message.message_id, reply_markup=courses_menu())
#
#     elif call.data in course_info:
#         bot.edit_message_text(course_info[call.data], call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=courses_menu())
#
#     elif call.data == "specialists":
#         bot.edit_message_text("📚 Mutaxassislarimiz:", call.message.chat.id, call.message.message_id, reply_markup=specialists_menu())
#
#     elif call.data in specialist_info:
#         bot.edit_message_text(specialist_info[call.data], call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=specialists_menu())
#
#     elif call.data == "about":
#         bot.edit_message_text(excel_masters_info, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=main_menu())
#
#     elif call.data == "contact":
#         bot.edit_message_text(contact_info_text, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=main_menu())
#
# # Botni ishga tushirish
# bot.polling(none_stop=True)




#
# import telebot
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# bot = telebot.TeleBot('7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ')  # Tokeningizni shu yerga qo‘ying
#
# # 🏠 Asosiy menyu
# def main_menu():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("📚 Mutaxassislarimiz", callback_data="specialists"))
#     markup.add(InlineKeyboardButton("📖 Kurslarimiz", callback_data="courses"))
#     markup.add(InlineKeyboardButton("ℹ️ Excel Masters haqida", callback_data="about"))
#     markup.add(InlineKeyboardButton("📞 Biz bilan bog‘lanish", callback_data="contact"))
#     return markup
#
# # 📖 Kurslar menyusi
# def courses_menu():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("🖥 Kompyuter Savodxonligi", callback_data="course_1"))
#     markup.add(InlineKeyboardButton("📊 Excel Boshlang‘ich", callback_data="course_2"))
#     markup.add(InlineKeyboardButton("📈 Excel Pro", callback_data="course_3"))
#     markup.add(InlineKeyboardButton("📉 Excel Pro Max", callback_data="course_4"))
#     markup.add(InlineKeyboardButton("⬅️ Asosiy menyu", callback_data="main_menu"))
#     return markup
#
# # 📚 Mutaxassislar menyusi
# def specialists_menu():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("👨‍🏫 Shoazim", callback_data="specialist_1"))
#     markup.add(InlineKeyboardButton("👨‍🏫 Feruzbek", callback_data="specialist_2"))
#     markup.add(InlineKeyboardButton("👨‍🏫 Begzod", callback_data="specialist_3"))
#     markup.add(InlineKeyboardButton("⬅️ Asosiy menyu", callback_data="main_menu"))
#     return markup
#
# # 📖 Kurslar haqida ma’lumot
# course_info = {
#     "course_1": "✅ **🖥 Kompyuter Savodxonligi**\n📌 Word, PowerPoint, Internet va fayl boshqaruvi\n📅 1-aprel 2025 | ⏳ 2 oy\n💰 500 000 so‘m/oyiga\n📋 Sertifikat beriladi!",
#     "course_2": "✅ **📊 Excel Boshlang‘ich**\n📌 Jadval yaratish, asosiy formulalar, diagrammalar\n📅 10-aprel 2025 | ⏳ 2,5 oy\n💰 600 000 so‘m/oyiga\n📋 Sertifikat beriladi!",
#     "course_3": "✅ **📈 Excel Pro**\n📌 Murakkab formulalar, Pivot jadval, avtomatlashtirish\n📅 20-aprel 2025 | ⏳ 3 oy\n💰 750 000 so‘m/oyiga\n📋 Sertifikat beriladi!",
#     "course_4": "✅ **📉 Excel Pro Max**\n📌 VBA, katta ma’lumotlar, avtomatlashtirish\n📅 5-may 2025 | ⏳ 4 oy\n💰 900 000 so‘m/oyiga\n📋 Sertifikat beriladi!"
# }
#
# # 📚 Mutaxassislar haqida ma’lumot
# specialist_info = {
#     "specialist_1": "👨‍🏫 **Shoazim**\n📌 7 yillik tajriba, Data Analyst\n📚 Excel, Power BI, SQL\n🎓 Microsoft sertifikati.",
#     "specialist_2": "👨‍🏫 **Feruzbek**\n📌 5 yillik tajriba, Excel treneri\n📚 Excel, Google Sheets\n🎓 Xalqaro sertifikat.",
#     "specialist_3": "👨‍🏫 **Begzod**\n📌 6 yillik tajriba, biznes analitik\n📚 Excel, Python, Power Query\n🎓 Data Science mutaxassisi."
# }
#
# # ℹ️ Excel Masters haqida
# excel_masters_info = "ℹ️ **Excel Masters** – Excel va Data Analysis bo‘yicha professional kurslar markazi.\n📌 Asosiy yo‘nalishlar: Excel, VBA, Power BI\n📍 Kurslar: onlayn va oflayn."
#
# # 📞 Bog‘lanish
# contact_info_text = "📞 **Biz bilan bog‘lanish:**\n📲 Telefon: +998 90 968 61 61\n✉️ Telegram: [@excelmasters_Shoazim](https://t.me/excelmasters_Shoazim)\n📍 Manzil: Toshkent, Chilonzor, Novza metrosi yonida."
#
# # 📩 Xabarlarni qayta ishlash
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f"Assalomu alaykum, {message.from_user.first_name} 👋 !\nExcel Masters kurslari haqida ma’lumot olish uchun quyidagi menyudan tanlang:", reply_markup=main_menu())
#
# # Callback handler
# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     if call.data == "main_menu":
#         bot.send_message(call.message.chat.id, "🏠 Asosiy menyu:", reply_markup=main_menu())
#
#     elif call.data == "courses":
#         bot.send_message(call.message.chat.id, "📖 Kurslarimiz:", reply_markup=courses_menu())
#
#     elif call.data in course_info:
#         bot.send_message(call.message.chat.id, course_info[call.data], parse_mode="Markdown", reply_markup=courses_menu())
#
#     elif call.data == "specialists":
#         bot.send_message(call.message.chat.id, "📚 Mutaxassislarimiz:", reply_markup=specialists_menu())
#
#     elif call.data in specialist_info:
#         bot.send_message(call.message.chat.id, specialist_info[call.data], parse_mode="Markdown", reply_markup=specialists_menu())
#
#     elif call.data == "about":
#         bot.send_message(call.message.chat.id, excel_masters_info, parse_mode="Markdown", reply_markup=main_menu())
#
#     elif call.data == "contact":
#         bot.send_message(call.message.chat.id, contact_info_text, parse_mode="Markdown", reply_markup=main_menu())
#
# # Botni ishga tushirish
# bot.polling(none_stop=True)



import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ"  # <-- Bot tokeningizni shu yerga qo‘ying
ADMIN_ID = 7442097952  # Admin (Call Center) ID'si

bot = telebot.TeleBot(TOKEN)

# 🏠 Asosiy menyu
def main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("📚 Mutaxassislarimiz", callback_data="specialists"),
        InlineKeyboardButton("📖 Kurslarimiz", callback_data="courses")
    )
    markup.add(
        InlineKeyboardButton("ℹ️ Excel Masters haqida", callback_data="about"),
        InlineKeyboardButton("📞 Biz bilan bog‘lanish", callback_data="contact")
    )
    return markup

# 📖 Kurslar menyusi
def courses_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🖥 Kompyuter Savodxonligi", callback_data="course_1"),
        InlineKeyboardButton("📊 Excel Boshlang‘ich", callback_data="course_2")
    )
    markup.add(
        InlineKeyboardButton("📈 Excel Pro", callback_data="course_3"),
        InlineKeyboardButton("📉 Excel Pro Max", callback_data="course_4")
    )
    markup.add(InlineKeyboardButton("⬅️ Orqaga", callback_data="main_menu"))
    return markup

# 📚 Mutaxassislar menyusi
def specialists_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("👨‍🏫 Shoazim", callback_data="spec_1"),
        InlineKeyboardButton("👨‍🏫 Feruzbek", callback_data="spec_2"),
        InlineKeyboardButton("👨‍🏫 Begzod", callback_data="spec_3")
    )
    markup.add(InlineKeyboardButton("⬅️ Orqaga", callback_data="main_menu"))
    return markup

# 📖 Kurslar haqida batafsil ma’lumot
course_info = {
    "course_1": "✅ **🖥 Kompyuter Savodxonligi**\n\n📌 Word va PowerPoint\n\n📌 Internet va e-mail\n\n📌 Windows va fayllar\n\n📅 1-aprel 2025\n\n⏳ 2 oy\n\n💰 500 000 so‘m/oyiga",
    "course_2": "✅ **📊 Excel Boshlang‘ich**\n\n📌 Jadval yaratish\n\n📌 Asosiy formulalar\n\n📌 Diagrammalar\n\n📅 10-aprel 2025\n\n⏳ 2,5 oy\n\n💰 600 000 so‘m/oyiga",
    "course_3": "✅ **📈 Excel Pro**\n\n📌 Murakkab formulalar\n\n📌 Filtrlash\n\n📌 Pivot jadval\n\n📅 20-aprel 2025\n⏳ 3 oy\n\n💰 750 000 so‘m/oyiga",
    "course_4": "✅ **📉 Excel Pro Max**\n\n📌 VBA dasturlash\n\n📌 Katta ma’lumotlar\n\n📌 Avtomatlashtirish\n\n📅 5-may 2025\n\n⏳ 4 oy\n\n💰 900 000 so‘m/oyiga"
}

# 📚 Mutaxassislar haqida batafsil ma’lumot
specialist_info = {
    "spec_1": "👨‍🏫 **Shoazim**\n\n📌 7 yillik tajriba\n\n📚 Excel, Power BI, SQL\n\n🎓 Microsoft sertifikati",
    "spec_2": "👨‍🏫 **Feruzbek**\n\n📌 5 yillik tajriba\n\n📚 Excel, Google Sheets\n\n🎓 Xalqaro sertifikat",
    "spec_3": "👨‍🏫 **Begzod**\n\n📌 6 yillik tajriba\n\n📚 Excel, Python, Power Query\n\n🎓 Data Science mutaxassisi"
}

# ℹ️ Excel Masters haqida
excel_masters_info = (
    "ℹ️ **Excel Masters** – Excel va Data Analysis bo‘yicha kurslar markazi.\n"
    "📍 2021-yilda tashkil etilgan\n\n"
    "👨‍💼 Asoschisi: Shahzod Sayfulla Begzod o‘g‘li\n\n"
    "‍💻 Microsoftning RASMIY hamkori\n\n"
    "🏆 3000+ muvaffaaqiyatli o‘quvchilar\n\n"
    "📌 Excel’da ishlash, VBA va Data Analysis bo‘yicha bilimlar beriladi."
)

# 📞 Bog‘lanish ma’lumotlari
contact_info_text = (
    "📞 **Biz bilan bog‘lanish:**\n"
    "📲 **Telefon:** +998 90 968 61 61\n"
    "✉️ **Telegram:** [@excelmasters_Shoazim](https://t.me/excelmasters_Shoazim)\n"
    "📍 **Manzil:** Toshkent, Chilonzor, Novza metro yonida"
)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "main_menu":
        bot.edit_message_text("🏠 Asosiy menyu:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
    elif call.data == "courses":
        bot.edit_message_text("📖 Kurslarimiz ro‘yxati:", call.message.chat.id, call.message.message_id, reply_markup=courses_menu())
    elif call.data == "specialists":
        bot.edit_message_text("📚 Bizning mutaxassislar:", call.message.chat.id, call.message.message_id, reply_markup=specialists_menu())
    elif call.data == "about":
        bot.edit_message_text(excel_masters_info, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=main_menu())
    elif call.data == "contact":
        # Telefon raqamini so‘rash tugmasi
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button = KeyboardButton("📞 Raqamni yuborish", request_contact=True)
        markup.add(button)

        # Foydalanuvchiga xabar
        bot.send_message(
            call.message.chat.id,
            "📞 Biz bilan bog‘lanish uchun quyidagilardan birini tanlang:\n\n"
            "📲 **Telefon orqali:** +998909686161\n"
            "✉️ **Telegram:** [@excelmasters_Shoazim](https://t.me/excelmasters_Shoazim)\n\n"
            "📍 [Bizning manzil](https://maps.app.goo.gl/b2zbEsXbFgc4f46dA)\n\n"
            "✅ Agar biz siz bilan bog‘lanishimizni istasangiz, pastdagi tugma orqali raqamingizni yuboring.",
            reply_markup=markup,
            parse_mode="Markdown"
        )

    elif call.data in course_info:
        bot.edit_message_text(course_info[call.data], call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=courses_menu())
    elif call.data in specialist_info:
        bot.edit_message_text(specialist_info[call.data], call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=specialists_menu())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        text = f"Assalamu alaykum, hurmatli {message.from_user.first_name}! 👋\n\n Excel Masters o'q'uv markaziga xush kelibsiz \n\n"
        "🔽 Kerakli bo‘limni tanlang:",
        reply_markup=main_menu()
    )


# 📞 Foydalanuvchi telefon raqamini yuborganida
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    phone_number = message.contact.phone_number
    user_name = message.from_user.first_name
    username = message.from_user.username  # Username olish
    username_text = f"@{username}" if username else "Username mavjud emas"

    # Foydalanuvchiga tasdiqlovchi xabar
    bot.send_message(
        message.chat.id,
        f"📞 Raqamingiz qabul qilindi: {phone_number}\n"
        f"📢 Call center tez orada siz bilan bog‘lanadi! ✅"
    )

    # Adminga xabar yuborish
    bot.send_message(
        ADMIN_ID,
        f"📩 **Yangi ro‘yxatdan o‘tish:**\n"
        f"📲 **Telefon:** +{phone_number}\n"
        f"🔗 **Username:** {username_text}"
    )

    # Asosiy menyuga qaytarish
    bot.send_message(message.chat.id, "🏠 Asosiy menyu:", reply_markup=main_menu())


# 🔄 Botni doimiy ishlash rejimiga qo‘yish
bot.polling(none_stop=True)


# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
#
# TOKEN = "7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ"  # <-- Bot tokeningizni shu yerga qo‘ying
# ADMIN_ID = 7442097952  # Admin ID
#
# bot = telebot.TeleBot(TOKEN)
#
# # Ro‘yxatdan o‘tgan foydalanuvchilarni saqlash
# registered_users = []
#
#
# # 🏠 Asosiy menyu
# def main_menu():
#     markup = InlineKeyboardMarkup(row_width=1)
#     markup.add(
#         InlineKeyboardButton("📚 Mutaxassislarimiz", callback_data="specialists"),
#         InlineKeyboardButton("📖 Kurslarimiz", callback_data="courses"),
#         InlineKeyboardButton("🔑 Admin paneli", callback_data="admin_panel")  # Admin paneli tugmasi
#     )
#     markup.add(
#         InlineKeyboardButton("ℹ️ Excel Masters haqida", callback_data="about"),
#         InlineKeyboardButton("📞 Biz bilan bog‘lanish", callback_data="contact")
#     )
#     return markup
#
#
# # 🔑 Admin paneli
# def admin_menu():
#     markup = InlineKeyboardMarkup(row_width=1)
#     markup.add(
#         InlineKeyboardButton("👥 Ro‘yxatdan o‘tganlar", callback_data="registered_users"),
#         InlineKeyboardButton("⬅️ Orqaga", callback_data="main_menu")
#     )
#     return markup
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     # 🔑 Admin paneli
#     if call.data == "admin_panel":
#         if call.message.chat.id == ADMIN_ID:
#             bot.edit_message_text(f"🔑 Xush kelibsiz, admin {call.message.from_user.first_name}!", call.message.chat.id,
#                                   call.message.message_id, reply_markup=admin_menu())
#         else:
#             bot.send_message(call.message.chat.id,
#                              f"❌ Bu bo‘lim faqat adminlar uchun, {call.message.from_user.first_name}!")
#
#     # 👥 Ro‘yxatdan o‘tgan foydalanuvchilar
#     elif call.data == "registered_users":
#         if call.message.chat.id == ADMIN_ID:
#             if registered_users:
#                 user_list = "\n".join(registered_users)
#                 bot.edit_message_text(f"📋 **Ro‘yxatdan o‘tgan foydalanuvchilar:**\n\n{user_list}", call.message.chat.id,
#                                       call.message.message_id, parse_mode="Markdown", reply_markup=admin_menu())
#             else:
#                 bot.edit_message_text("📋 Hozircha hech kim ro‘yxatdan o‘tmagan.", call.message.chat.id,
#                                       call.message.message_id, reply_markup=admin_menu())
#
#     elif call.data == "main_menu":
#         bot.edit_message_text("🏠 Asosiy menyu:", call.message.chat.id, call.message.message_id,
#                               reply_markup=main_menu())
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(
#         message.chat.id,
#         f"Assalamu alaykum, hurmatli {message.from_user.first_name}! 👋\n\n🔽 Kerakli bo‘limni tanlang:",
#         reply_markup=main_menu()
#     )
#
#
# # 📞 Foydalanuvchi telefon raqamini yuborganida
# @bot.message_handler(content_types=['contact'])
# def handle_contact(message):
#     phone_number = message.contact.phone_number
#     user_name = message.from_user.first_name
#     username = message.from_user.username  # Username olish
#     username_text = f"@{username}" if username else "Username mavjud emas"
#
#     # Ro‘yxatga qo‘shish
#     registered_users.append(f"👤 {user_name} | 📞 {phone_number} | 🔗 {username_text}")
#
#     # Foydalanuvchiga tasdiqlovchi xabar
#     bot.send_message(
#         message.chat.id,
#         f"📞 Raqamingiz qabul qilindi: {phone_number}\n"
#         f"📢 Call center tez orada siz bilan bog‘lanadi! ✅"
#     )
#
#     # Adminga xabar yuborish
#     bot.send_message(
#         ADMIN_ID,
#         f"📩 **Yangi ro‘yxatdan o‘tish:**\n"
#         f"👤 **Ism:** {user_name}\n"
#         f"📲 **Telefon:** {phone_number}\n"
#         f"🔗 **Username:** {username_text}"
#     )
#
#     # Asosiy menyuga qaytarish
#     bot.send_message(message.chat.id, "🏠 Asosiy menyu:", reply_markup=main_menu())
#
#
# # 🔄 Botni doimiy ishlash rejimiga qo‘yish
# bot.polling(none_stop=True)
