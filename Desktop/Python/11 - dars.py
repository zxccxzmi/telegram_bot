family = {
    1: {"Name": "Dilshod",
         "age": 55
    },
    2: {"Name": "Lola",
        "age": 48
    },
    3: {"Name": "Muhammad Ibrohim",
        "age": 16
        }}
#
#
# //////
warehouse = {
    "Olma": {"narx": 12000, "soni": 50},
    "Banan": {"narx": 18000, "soni": 30},
    "Uzum": {"narx": 15000, "soni": 40},
}
max_price_product = None
total_count = 0
#
for product in warehouse.items():
    total_count += product[1]["soni"]
    if max_price_product is None:
        max_price_product = product
    else:
        if product[1].get("narx") > max_price_product[1].get("narx"):
# /#             max_price_product = product
#
print(f"{max_price_product[0]}: {max_price_product[1]['narx']} so'm")
print(f"Total count: {total_count}")
#
# contacts = {
#     "ALi": "+998938719010",
#     "Gani": "+998938719020",
#     "VaLi": "+998938719030",
# }
#
# phone_number = input("Enter your phone number: ")
#
# if phone_number == "+998938719010":
#     print("ALi")
# elif phone_number == "+998938719020":
#     print("Gani")
# else:
#     print("VaLi")