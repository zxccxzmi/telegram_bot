# import random
#
# def viktorina():
#     savollar = [
#         {
#             "savol": "Python dasturlash tili qachon yaratilgan?",
#             "variantlar": ["A) 1991", "B) 2000", "C) 1989", "D) 2010"],
#             "t_javob": "A"
#         },
#         {
#             "savol": "Dunyo bo'yicha eng ko‘p ishlatiladigan dasturlash tili qaysi?",
#             "variantlar": ["A) Java", "B) Python", "C) C++", "D) JavaScript"],
#             "t_javob": "B"
#         },
#         {
#             "savol": "Python tilining asoschisi kim?",
#             "variantlar": ["A) Dennis Ritchie", "B) James Gosling", "C) Guido van Rossum", "D) Bjarne Stroustrup"],
#             "t_javob": "C"
#         }
#     ]
#
#     # Tasodifiy savolni tanlash
#     savol = random.choice(savollar)
#
#     print("\n" + savol["savol"])
#     for variant in savol["variantlar"]:
#         print(variant)
#
#     javob = input("\nTo‘g‘ri javobni tanlang (A, B, C yoki D): ").strip().upper()
#
#     if javob == savol["t_javob"]:
#         print("✅ To‘g‘ri javob!")
#     else:
#         print(f"❌ Xato! To‘g‘ri javob: {savol['t_javob']}")
#
# if __name__ == "__main__":
#     while True:
#         viktorina()
#         yana = input("\nYana bir savolni ko‘rishni istaysizmi? (ha/yo'q): ").strip().lower()
#         if yana != "ha":
#             print("Rahmat! Viktorina tugadi.")
#             break