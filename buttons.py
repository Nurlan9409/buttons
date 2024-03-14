from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



button1 = ReplyKeyboardMarkup(resize_keyboard=True)
button1.add(KeyboardButton('Menu'))
button1.add(KeyboardButton('Boshqa sevislar'))


button_1= ReplyKeyboardMarkup(resize_keyboard=True)
button_1.add(KeyboardButton('Taomlar'))
button_1.add(KeyboardButton('Fast_food'))
button_1.add(KeyboardButton('Ichimliklar'))


taom_menu = ReplyKeyboardMarkup(resize_keyboard=True)

taom_menu.add(KeyboardButton('Beshbarmoq'))
taom_menu.add(KeyboardButton('Toy oshi'))
taom_menu.add(KeyboardButton('Norin'))
taom_menu.add(KeyboardButton('Monti'))
taom_menu.add(KeyboardButton('Shorva'))
taom_menu.add(KeyboardButton('Back'))

fast_food_menu = ReplyKeyboardMarkup(resize_keyboard=True)
fast_food_menu.add (KeyboardButton('Lavash'))
fast_food_menu.add (KeyboardButton('Donar'))
fast_food_menu.add (KeyboardButton('Non kabob'))
fast_food_menu.add (KeyboardButton('Burger'))
fast_food_menu.add(KeyboardButton('Back'))

water_menu = ReplyKeyboardMarkup(resize_keyboard=True)
water_menu.add (KeyboardButton('Milliy Kola'))
water_menu.add (KeyboardButton('Dinay '))
water_menu.add (KeyboardButton('Ace tea'))
water_menu.add (KeyboardButton('Limon choy'))
water_menu.add(KeyboardButton('Back'))












