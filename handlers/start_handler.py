from aiogram import Router, F, types
from aiogram.types import Message
from aiogram.filters import Command
import keyboards
import consts

router = Router()


@router.message(Command("start"))
async def start(msg: Message):
    await msg.answer(consts.START_MESSAGE, reply_markup=keyboards.create_start_kb())


@router.message(F.text == "История Смоленска")
async def history(msg: Message):
    await msg.answer("Здесь будет история Смоленска", reply_markup=keyboards.ReplyKeyboardRemove())


@router.message(F.text == "Квесты")
async def quests(msg: Message):
    await msg.answer("Здесь будут квесты", reply_markup=keyboards.ReplyKeyboardRemove())


@router.message(Command("help"))
async def help(msg: Message):
    await msg.answer(consts.get_help_message())


