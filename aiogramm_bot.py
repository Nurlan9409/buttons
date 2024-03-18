import os
import logging
from db_base import Database
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
load_dotenv()
from buttons import button_1, taom_menu, fast_food_menu, water_menu,keyboard, keyboard_1,pay_type,inline_kb4,water

API_TOKEN = os.getenv('BOT_TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.callback_query_handler(lambda c: c.data == "Geolokasiyani jonating")
async def process_callback_button_menu(callback_query: types.CallbackQuery, message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    await bot.answer_callback_query(callback_query.id ,cache_time=0)
    await bot.send_message(callback_query.from_user.id, lat, lon)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = message.chat.id
    check_query ="""select * from info_users where chat_id = '{chat_id}'"""
    if len(Database.connect(check_query,"select")) >= 1:
        await message.answer(f"Hey whats_up{username}", reply_markup= button_1)
    else:

        print(f"Username: {username} star_bot")
        query =f"""insert into info_users(first_name, last_name, username,chat_id) values ('{first_name}', '{last_name}', '{username}','{chat_id}')"""
        print(f"{username} {Database.connect(query,"insert")}")
        await message.answer(f"Assalomualeykum menuni tanlang {username}",reply_markup= button_1)





@dp.message_handler(lambda message : message.text == 'Menu')
async def menu(message: types.Message):
    await message.answer('Menu', reply_markup=button_1)


@dp.message_handler(lambda message: message.text == "Taomlar")
async def taomlar(message: types.Message):
     await message.answer("Taomni tanlang", reply_markup=taom_menu)

@dp.message_handler(lambda message: message.text== 'Toy oshi')
async def osh(message: types.Message):
    await message.answer('Porsiyani Tanlang', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Yarim porsiya')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang',reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == 'Bir porsiya')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang',reply_markup=pay_type)


@dp.message_handler(lambda message: message.text== 'Norin')
async def norin(message: types.Message):
    await message.answer('Porsiyani Tanlang', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Yarim porsiya')
async def porsiya(message: types.Message):
    await message.answer('tolov turini tanlang',reply_markup=pay_type)

@dp.message_handler(lambda message: message.text == 'Bir porsiya')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang',reply_markup=pay_type)


@dp.message_handler(lambda message: message.text== 'Monti')
async def monti(message: types.Message):
    await message.answer('Porsiyani Tanlang', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Bir porsiya')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang',reply_markup=pay_type)




@dp.message_handler(lambda message: message.text == 'Yarim porsiya')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang',reply_markup=pay_type)

@dp.message_handler(lambda message: message.text == 'Bir porsiya')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang',reply_markup=pay_type)





@dp.message_handler(lambda message: message.text== 'Beshbarmoq')
async def beshbarmoq(message: types.Message):
    await message.answer('Porsiyani Tanlang', reply_markup=keyboard)



@dp.message_handler(lambda message: message.text == 'Yarim porsiya')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang',reply_markup=pay_type)

@dp.message_handler(lambda message: message.text == 'Bir porsiya')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang',reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == "Fast_food")
async def fast_food(message: types.Message):
     await message.answer("Fastfoodni tanlang", reply_markup=fast_food_menu)



@dp.message_handler(lambda message: message.text == 'Lavash')
async def lavash(message: types.Message):
    await message.answer('Lavash Turini Tanlang', reply_markup=keyboard_1)


@dp.message_handler(lambda message: message.text == 'Small')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == 'Standart')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == 'Big')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)

@dp.message_handler(lambda message: message.text == 'Donar')
async def donar(message: types.Message):
    await message.answer('Donar Turini Tanlang', reply_markup=keyboard_1)


@dp.message_handler(lambda message: message.text == 'Small')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == 'Standart')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == 'Big')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == 'Non kabob')
async def non_kabob(message: types.Message):
    await message.answer('Non kabob Turini Tanlang', reply_markup=keyboard_1)


@dp.message_handler(lambda message: message.text == 'Small')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == 'Standart')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == 'Big')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)

@dp.message_handler(lambda message: message.text == 'Burger')
async def burger(message: types.Message):
    await message.answer('Burger Turini Tanlang', reply_markup=keyboard_1)


@dp.message_handler(lambda message: message.text == 'Small')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == 'Standart')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == 'Big')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)



@dp.message_handler(lambda message: message.text == "Ichimliklar")
async def ichimliklar(message: types.Message):
     await message.answer("Ichimlikni tanlang", reply_markup=water_menu)


@dp.message_handler(lambda message:message.text == "Milliy Kola")
async def milliy_kola(message: types.Message):
    await message.answer("Nechi litrli tanlang", reply_markup=water)


@dp.message_handler(lambda message: message.text == '0.5')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)

@dp.message_handler(lambda message: message.text == '1')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)

@dp.message_handler(lambda message: message.text == '1.5')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == "Dinay")
async def milliy_kola(message: types.Message):
    await message.answer("Nechi litrli tanlang", reply_markup=water)


@dp.message_handler(lambda message: message.text == '0.5')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == '1')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == '1.5')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == "Ice tea")
async def milliy_kola(message: types.Message):
    await message.answer("Nechi litrli tanlang", reply_markup=water)


@dp.message_handler(lambda message: message.text == '0.5')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == '1')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)


@dp.message_handler(lambda message: message.text == '1.5')
async def porsiya(message: types.Message):
    await message.answer('Zakazingiz qabul qilindi, Geolokasiya jonating', reply_markup=inline_kb4)
    await message.answer('tolov turini tanlang', reply_markup=pay_type)





@dp.message_handler(lambda message:message.text =="Back")
async def back_menu(message: types.Message):
     await message.answer("Menuga qaytish",reply_markup=button_1)


class MyClass:
    location = None

    @dp.callback_query_handler(lambda c: c.data == "btn_geo")
    async def process_callback_button_menu(callback_query: types.CallbackQuery):
        MyClass.location = callback_query.location
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, "Спасибо! Теперь вы можете отправить мне сообщение с вашим вопросом.")

@dp.message_handler(lambda message:message.text=="btn_geo")
async def handle_text_message(message: types.Message):
    if MyClass.location is not None:
        lat = MyClass.location.latitude
        lon = MyClass.location.longitude
        MyClass.location = None
        await bot.send_message(message.chat.id, f"Sizning geolokasiyangiz: {lat}, {lon}", reply_markup= inline_kb4)
    else:

        await bot.send_message(message.chat.id, "Iltimos geolokasiya jonating")

@dp.message_handler(commands=['data'])
async def data_callback(message: types.Message):
    if message.from_user.id ==[810523537]:
        await message.reply("Hi admin")
    else:
        await message.reply("Bunday maklumot topilmadi")



@dp.message_handler(commands=['data'])
async def data_callback(message: types.Message):
    query = """select * from admins"""
    admins = []
    for i in  Database.connect(query,"select"):
       admins.append(i[1])
    if message.from_user.id in admins:
        await message.reply("Hi admin")
    else:
        await message.reply("Bunday maklumot topilmadi")







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
