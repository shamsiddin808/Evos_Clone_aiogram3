import logging
from itertools import product
from linecache import clearcache
from xml.dom.expatbuilder import TEXT_NODE

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.types import ContentType, Message, InputFile
from aiogram.types import ContentType
from states.state import MyStates


from aiogram import types
import re

from databace import cursor, register_user, add_location, delete_accaunt_databace

from buttons.default import keyboard, location, main_menu, delete_accaunt, setlar

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_TOKEN = '6864628672:AAFxap26WZK8aboLm33XHdXUJCm35KDW8Rk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
@dp.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    user_filter = cursor.execute("SELECT * FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
    if user_filter is None:
        await message.reply(f"<b>Salom {message.from_user.full_name}\nBizni bo'timizdan foydalanish uchun <i>Telefon</i> raqamingizni yuboring📞</b>", reply_markup=keyboard, parse_mode="HTML")
    else:
        await message.reply("<b>Assalomu Aleykum Evos Dastavka Bo'tiga Xush kelibsiz😊\nSiz bosh menudasiz📖</b>", reply_markup=main_menu,parse_mode="HTML")


@dp.message(F.content_type == ContentType.CONTACT)
async def phone_register(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    phone = message.contact.phone_number
    await register_user(user_id, phone)
    await message.reply("<b>Iltimos <i>lakatsiya</i> yuboring</b>", reply_markup=location, parse_mode="HTML")


@dp.message(F.content_type == ContentType.LOCATION)
async def phone_register(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    longitude = message.location.longitude
    latitude = message.location.latitude
    await add_location(longitude, latitude, user_id)
    await message.reply("<b>Siz muvofaqiyatli ro'yxatdan o'tdingiz🎉</b>", reply_markup=main_menu, parse_mode="HTML")


@dp.message(F.text == "Sozlanmalar⚙️")
async def text_messages(message: types.Message):
    await message.reply("<b><i>Sozlanmalar</i> bo'limiga xush kelibsiz🛠</b>", reply_markup=delete_accaunt,
                        parse_mode="HTML")


@dp.message(F.text == "Akkauntni ochirish🗑")
async def text_messages(message: types.Message):
    await delete_accaunt_databace(message.from_user.id)
    await message.reply("Sizning akkauntingiz muvoqiyatli o'childi✔️", reply_markup=main_menu, parse_mode="HTML")

@dp.message(F.text == "Setlar🍟")
async def text_messages(message: types.Message):
    await message.reply("<b><i>Setlar🍟</i> bo'limiga xush kelibsiz🙈</b>", reply_markup=setlar, parse_mode="HTML")
@dp.message(F.text == "Setlar Fri🍟")
async def setlar_message(message: types.Message):
    fri_filter = cursor.execute("SELECT * FROM products WHERE name = ?", ("Setlar Fri🍟",)).fetchone()
    if fri_filter:
        photo_path = fri_filter[0]
        caption = f"\nFood nomi: {fri_filter[1]}\n\nNarxi: {fri_filter[2]}"
        with open(photo_path, "rb") as image:
            await message.answer_photo(image, caption=caption)
    else:
        await message.reply("Tavar mavjud emas.")


@dp.message(F.text == "Orqaga🔙")
async def text_messages(message: types.Message):
    await message.reply("<b>Siz bosh menudasiz📖</b>", reply_markup=main_menu, parse_mode="HTML")



# @dp.message(F.text.regexp(r"\d+"))
# async def numbers_message(message: types.Message):
#     await message.reply("Bu xabar raqamlar o'z ichiga oladi.")

@dp.message()
async def echo_message(message: types.Message):
    await message.reply(message.text)




async def main():
    try:
        print("Bot ishga tushmoqda...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("Bot seansi yopildi")
if __name__ == "__main__":
    asyncio.run(main())
