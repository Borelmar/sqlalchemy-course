from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from config import settings
import database


bot = Bot(
    token=settings.TG_TOKEN,
    default=DefaultBotProperties(
        parse_mode="HTML",
        link_preview_is_disabled=True
    ),
)

dp = Dispatcher(bot=bot)

@dp.message_handler(Command('search'))
async def search_handler(message: Message, command: CommandObject):
    #res = await database.test()
    await message.answer(command.args)

async def start_bot():
    await dp.start_polling(bot)