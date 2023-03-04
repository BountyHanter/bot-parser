from aiogram import Bot, Dispatcher, types, executor
from keyboards import kb, kb1, ikb1, ikb2, ikb3, ikb3__1
import random
import string
from Data_output import output
import asyncio
from undetected_driver import take_html
from database import drop
import os

TEXT = """
Кнопки для бота находятся справа в строке ввода\(Или слева в списке\)

/random \- рандомная буква
/start \- начать работу
/description \- описание бота и мой вк
/sticker \- получить стикер
/idsticker \- получить id стикера \(в разработке\)
/meme \- отправит мемас
/parser \- запустить парсер
"""
sent_sticker = False
bot = Bot(token='6249292999:AAFK1mI59IrKMvlC8JRWbIAilp8nbOG_lUQ')
dp = Dispatcher(bot)


async def on_startup(_):
    print("Бот запущен!")


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text='*Доступные команды:*\n' + TEXT,
                         parse_mode=types.ParseMode.MARKDOWN_V2,
                         reply_markup=kb)


@dp.message_handler(commands=['description'])
async def desc_comm(message: types.Message):
    await message.answer(text='Этот бот \- мой пет проект, я сюда сую всё чему учусь',
                         parse_mode=types.ParseMode.MARKDOWN_V2,
                         reply_markup=ikb1)
    await message.answer('это сообщение чтобы появилась кнопка', reply_markup=kb1)


@dp.message_handler(commands=['random'])
async def random_letter(message: types.Message):
    await message.answer(random.choice(string.ascii_letters))


@dp.message_handler(commands=['sticker'])
async def random_letter(message: types.Message):
    await message.answer(text='Чел, твоя просьба это')
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEH2V5j9a3kDUz4DO5rCDzQ6R21zrGrjQACIQADumTPDwIruQwj7FhxLgQ")


"""@dp.message_handler(commands=['idsticker'])
async def handle_sticker_command(message: types.Message):
    await message.answer("Ну давай твой стикер...")

    # Use another handler to wait for a sticker message
    @dp.message_handler(content_types=types.ContentTypes.STICKER)
    async def handle_sticker(message: types.Message):
        # Get the sticker ID and send it as a message
        sticker_id = message.sticker.file_id
        await message.answer(f"ID этого стикера - {sticker_id}")


    # Use another handler to wait for a non-sticker message
    @dp.message_handler(content_types=types.ContentTypes.ANY)
    async def handle_non_sticker(message: types.Message):
        # Send an error message and ask for a sticker again
        await message.answer("Чел, ты дурак? стикер отправляй или отвали... (Вводи заного /idsticker)")"""


@dp.message_handler(commands=['meme'])
async def random_letter(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://i.imgur.com/aLhAw5a.png',
                         reply_markup=ikb2)


parsing_mode = False
continue_parsing = False

@dp.message_handler(commands=['parser'])
async def random_letter(message: types.Message):
    global parsing_mode
    parsing_mode = True
    await message.answer("Введите товар, который хотите спарсить\n(если передумал напиши stop)")

@dp.callback_query_handler()
async def random_callback(callback: types.CallbackQuery):
    match callback.data:
        case 'crandom':
            await callback.message.answer(random.choice(string.ascii_letters))
            await callback.message.delete()
        case 'backstart':
            await help_command(callback.message)
            await callback.message.delete()
            await drop()
        case 'next5elem':
            global continue_parsing
            continue_parsing = True
            await callback.message.delete()

@dp.message_handler()
async def answer(message: types.Message):
    await message.answer("Парсинг начался, если ничего не появится через секунд 7 то нажми еще раз /parser")
    global parsing_mode
    if parsing_mode:
        if message.text.lower() == 'stop'.lower():
            parsing_mode = False
            await message.answer("Парсинг остановлен")
            return  # Add this line to exit the function
        take_html(message.text)
        data = output()
        ln = len(data)
        for idx, count in enumerate(data):
            await bot.send_photo(chat_id=message.chat.id,
                                 photo=count['picture_link'],
                                 caption=(
                                     f'{count["name"]}\n\n'
                                     f'💰Цена: {count["price"]} рублей\n'
                                     f'⭐Рейтинг: {count["rating"]}\n'
                                     f'📔Колличество отзывов: {count["num_revives"]}\n'
                                     f'🔗Ссылка на товар:\n{count["product_link"]}'
                                 ))
            if idx % 5 == 4:
                global continue_parsing
                await message.answer(text=f'Показано {idx+1} элементов из {ln}', reply_markup=ikb3)
                continue_parsing = False
                while not continue_parsing:
                    await asyncio.sleep(1)
                if continue_parsing is True:
                    continue
            parsing_mode = False
        await message.answer(text="Все товары показаны", reply_markup=ikb3__1)
        await drop()
    else:
        await message.answer(text="Я не умею понимать текст пока что, только команды")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
