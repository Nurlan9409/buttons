import os
import logging
from db_base import Database
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
load_dotenv()
from buttons import button_1,taom_menu,button1,fast_food_menu,water_menu

API_TOKEN = os.getenv('BOT_TOKEN')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = message.chat.id
    check_query ="""select * from info_users where chat_id = '{chat_id}'"""
    if len(Database.connect(check_query,"select")) >= 1:
        await message.answer(f"Hey whats_up{username}", reply_markup= button1)
    else:

        print(f"Username: {username} star_bot")
        query =f"""insert into info_users(first_name, last_name, username,chat_id) values ('{first_name}', '{last_name}', '{username}','{chat_id}')"""
        print(f"{username} {Database.connect(query,"insert")}")
        await message.answer(f"Assalomualeykum menuni tanlang {username}",reply_markup= button1)





@dp.message_handler()
async def echo(message: types.Message):
    user_username = message.from_user.username

    await message.answer(message.text)


@dp.message_handler(lambda message:message.text =='Menu')
async def menu(message: types.Message):
     await message.answer('Menu', reply_markup=button_1)
     await message.answer("Нажмите на кнопку", reply_markup=button_1)


@dp.message_handler(lambda message: message.text == "Taomlar")
async def taomlar(message: types.Message):
     await message.answer("Taomni tanlang", reply_markup=taom_menu)
@dp.message_handler(lambda message: message.text == "Fast_food")
async def taomlar(message: types.Message):
     await message.answer("Fastfoodni tanlang", reply_markup=fast_food_menu)

@dp.message_handler(lambda message: message.text == "Ichimliklar")
async def taomlar(message: types.Message):
     await message.answer("Ichimlikni tanlang", reply_markup=water_menu)

@dp.message_handler(lambda message:message.text =="Back")
async def back_menu(message: types.Message):
     await message.answer("Menuga qaytish",reply_markup=button_1)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
