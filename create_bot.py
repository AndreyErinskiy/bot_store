from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='5903774545:AAFZMLBH3rbzMjjR2r2Vb_W10sgabK97EW0')
dp = Dispatcher(bot, storage=storage)

