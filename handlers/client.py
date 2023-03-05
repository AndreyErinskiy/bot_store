from aiogram import types
from bot_telegram import dp
from create_bot import bot


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Хороших покупок)')
        await message.delete()
    except:
        await message.reply('Общение с ботом через Лс, напишите ему :\nhttps://t.me/posh_nvkz_bot')


@dp.message_handler(commands=['rules'])
async def order_conditions(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПРОПИСАТЬ УСЛОВИЯ ДЛЯ ЗАКАЗА')


@dp.message_handler(commands=['Реквизиты'])
async def money_send(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПРОПИСАТЬ РЕКВИЗТЫ ДЛЯ ПРИЕМА ДЕНЕГ')

# @dp.message_handler(commands=['Меню'])
# async def shop_menu_commands(message : types.Message):
#     for ret in cur.execute('SELECT * FROM menu').fetchall():
#         await bot.send_message(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
