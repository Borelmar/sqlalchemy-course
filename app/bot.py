from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, CommandObject
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from config import settings
import database
import models

bot = Bot(
    token=settings.TG_TOKEN,
    default=DefaultBotProperties(
        parse_mode="HTML",
        link_preview_is_disabled=True
    )
)

dp = Dispatcher(bot=bot)

class AddVacancyStates(StatesGroup):
    enter_title = State()
    enter_body = State()



@dp.message(Command('search'))
async def search_handler(message: Message, command: CommandObject):
    if command.args == None:
        await   message.answer('Error argument')
    else:
        words = command.args.strip()
        vacancies = await database.search_vacancy(words)
        for vacancy in vacancies:
            title = vacancy.title
            body = vacancy.body
            vacancy_fmt = f"<b>{title}</b>\n\n{body}"
            await message.answer(vacancy_fmt)

@dp.message(Command('show'))
async def show_handler(message: Message):
    vacancies = await database.get_all_vacancies()
    for vacancy in vacancies:
        title = vacancy.title
        body = vacancy.body
        vacancy_fmt = f"<b>{title}</b>\n\n{body}"
        await message.answer(vacancy_fmt)


@dp.message(Command('add'))
async def add_handler_1(message: Message, state: FSMContext):
    await state.set_state(AddVacancyStates.enter_title)
    await message.answer('Введите заголовок:')

@dp.message(AddVacancyStates.enter_title)
async def add_handler_2(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(AddVacancyStates.enter_body)
    await message.answer('Введите тело вакансии:')

@dp.message(AddVacancyStates.enter_body)
async def add_handler_3(message: Message, state: FSMContext):
    await state.update_data(body=message.text)
    data = await state.get_data()
    vacancy = models.Vacancy(title=data['title'], body=data['body'])
    await database.add_vacancy(vacancy)
    await message.answer('Ваша вакасния успешно добавленна!')


async def start_bot():
    await dp.start_polling(bot)