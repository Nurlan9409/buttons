from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types


keyboard = types.InlineKeyboardMarkup()
inline1 = types.InlineKeyboardButton(text=" Yarim porsiya", callback_data="Taom_porsiya")
inline2 = types.InlineKeyboardButton(text=" Bir porsiya", callback_data="Taom_porsiya")
inline3 = types.InlineKeyboardButton(text=" Ikki kishilik", callback_data="Taom_porsiya")
inline4 = types.InlineKeyboardButton(text=" Ortga", callback_data="Taom_porsiya")
keyboard.add(inline1, inline2,inline3,
             inline4)





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
water_menu.add (KeyboardButton('Ace tea'))
water_menu.add (KeyboardButton('Limon choy'))
water_menu.add(KeyboardButton('Back'))

but = types.InlineKeyboardButton("Geolokasiyani jonating", request_location=True, callback_data='btn_geo')

inline_kb4 = InlineKeyboardMarkup().add(but)

keyboard_1 = types.InlineKeyboardMarkup()
inline_1 = types.InlineKeyboardButton(text=" Small", callback_data="lavash turi")
inline_2 = types.InlineKeyboardButton(text=" Big", callback_data="lavash turi")
inline_4 = types.InlineKeyboardButton(text=" Ortga", callback_data="lavash turi")
keyboard.add(inline_1, inline_2,
             inline_4)
















