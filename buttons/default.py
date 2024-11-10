from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from databace import register_user

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Send number📱", request_contact=True),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Send location", request_location=True),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Setlar🍟"),
            KeyboardButton(text="Karzinka🛒")
        ],
        [
            KeyboardButton(text="Sozlanmalar⚙️")
        ],
        [
            KeyboardButton(text="Orqaga🔙")
        ]
    ],
    resize_keyboard=True,
)

ha_yoq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha✅"),
            KeyboardButton(text="Yoq❌")
        ],
        [
            KeyboardButton(text="Orqaga🔙")

        ]
    ],
    resize_keyboard=True,
)


delete_accaunt = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Akkauntni ochirish🗑"),
            KeyboardButton(text="Orqaga🔙")
        ]
    ],
    resize_keyboard=True,
)

setlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Setlar Fri🍟"),
            KeyboardButton(text="Yashil set🟩"),

        ],

        [
            KeyboardButton(text="Ramazon Set🥓")
        ],
        [
            KeyboardButton(text="Orqaga🔙")
        ]

    ],
    resize_keyboard=True,
)