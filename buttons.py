from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, inline_keyboard
from aiogram import types


keyboard = types.InlineKeyboardMarkup()
inline1 = types.InlineKeyboardButton(text=" Yarim porsiya", callback_data="Taom_porsiya")
inline2 = types.InlineKeyboardButton(text=" Bir porsiya", callback_data="Taom_porsiya")
inline3 = types.InlineKeyboardButton(text=" Ikki kishilik", callback_data="Taom_porsiya")
inline4 = types.InlineKeyboardButton(text=" Ortga", callback_data="Taom_porsiya")
keyboard.add(inline1, inline2,inline3,
             inline4)

pay_type = types.InlineKeyboardMarkup()
pay_type2=types.InlineKeyboardButton("click",callback_data="pay_type")
pay_type3=types.InlineKeyboardButton("pay_me",callback_data="pay_type")
pay_type4=types.InlineKeyboardButton("apelsin",callback_data="pay_type")
pay_type5=types.InlineKeyboardButton("uzum_bank",callback_data="pay_type")
pay_type6=types.InlineKeyboardButton("apelsin",callback_data="pay_type")
keyboard.add(
             pay_type2,pay_type3,
             pay_type4,pay_type5,pay_type6)





button_1= ReplyKeyboardMarkup(resize_keyboard=True)
button_1.add(KeyboardButton('Taomlar'))
button_1.add(KeyboardButton('Fast_food'))
button_1.add(KeyboardButton('Ichimliklar'))


taom_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

taom_menu.add(KeyboardButton('Beshbarmoq'))
taom_menu.add(KeyboardButton('Toy oshi'))
taom_menu.add(KeyboardButton('Norin'))
taom_menu.add(KeyboardButton('Monti'))
taom_menu.add(KeyboardButton('Shorva'))
taom_menu.add(KeyboardButton('Back'))

fast_food_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
fast_food_menu.add (KeyboardButton('Lavash'))
fast_food_menu.add (KeyboardButton('Donar'))
fast_food_menu.add (KeyboardButton('Non kabob'))
fast_food_menu.add (KeyboardButton('Burger'))
fast_food_menu.add(KeyboardButton('Back'))

water_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
water_menu.add (KeyboardButton('Milliy Kola'))
water_menu.add (KeyboardButton('Dinay '))
water_menu.add (KeyboardButton('Ice tea'))
water_menu.add(KeyboardButton('Back'))

but = types.InlineKeyboardButton("geolokasiya", request_location=True, callback_data='geolokasiya')

inline_kb4 = InlineKeyboardMarkup()
inline_kb4= types.InlineKeyboardButton("geolokasiya jonating", callback_data='btn_geo')

keyboard_1 = types.InlineKeyboardMarkup()
inline_1 = types.InlineKeyboardButton(text=" Small", callback_data="fast_food turi")
inline_2= types.InlineKeyboardButton(text=" Standart", callback_data="fast_food turi")
inline_3 = types.InlineKeyboardButton(text=" Big", callback_data="fast_food turi")
inline_4 = types.InlineKeyboardButton(text=" Ortga", callback_data="fast_food turi")
keyboard_1.add(inline_1, inline_2,
               inline_3, inline_4)



water = types.InlineKeyboardMarkup()
water_size = types.InlineKeyboardButton(text="0.5l")
water_size1= types.InlineKeyboardButton(text="1l")
water_size2 = types.InlineKeyboardButton(text="1.5l")
water.add(water_size,
          water_size1,
          water_size2)

















