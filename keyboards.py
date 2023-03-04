from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/description')
b2 = KeyboardButton('/random')
b3 = KeyboardButton('/sticker')
b4 = KeyboardButton('/meme')
b5 = KeyboardButton('/start')
b6 = KeyboardButton('/parser')
kb.add(b1).insert(b2).add(b3).insert(b4).add(b6)
kb1.add(b5)

ikb1 = InlineKeyboardMarkup(row_width=2)
ikb2 = InlineKeyboardMarkup(row_width=3)
ikb3 = InlineKeyboardMarkup(row_width=2)
ikb3__1 = InlineKeyboardMarkup(row_width=2)
ikb1_1 = InlineKeyboardButton(text="Мой ВК",
                            url='https://vk.com/id_asasin_cross')
ikb1_2 = InlineKeyboardButton(text="Получить рандомную букву",
                              callback_data='crandom')
ikb2_1 = InlineKeyboardButton(text="Зачетная пикча👍",
                              callback_data="like")
ikb2_2 = InlineKeyboardButton(text="Конкретно зачетная пикча😍",
                              callback_data="VeryLike")
ikb2_3 = InlineKeyboardButton(text='👈Вернутся в старт',
                              callback_data='backstart')
ikb3_1 = InlineKeyboardButton(text="Следующие 5 элементов",
                              callback_data='next5elem')
ikb3_2 = InlineKeyboardButton(text="Завершить парсинг",
                              callback_data='backstart')
ikb3_3 = InlineKeyboardButton(text="Вернутся на главную",
                              callback_data='backstart')

ikb1.add(ikb1_1).add(ikb1_2)
ikb2.add(ikb2_1,ikb2_2).add(ikb2_3)
ikb3.add(ikb3_1,ikb3_2)
ikb3__1.add(ikb3_3)
