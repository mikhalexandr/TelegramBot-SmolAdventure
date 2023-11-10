from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
import keyboards
import consts
import states

router = Router()


@router.message(Command("start"))
async def start(msg: Message):
    await msg.answer(consts.START_MESSAGE, reply_markup=keyboards.create_start_kb())


@router.message(F.text == "История Смоленска")
async def history(msg: Message, state: FSMContext):
    await msg.answer("Здесь будет история Смоленска", reply_markup=keyboards.ReplyKeyboardRemove())


@router.message(F.text == "Квесты")
async def quests(msg: Message, state: FSMContext):
    await msg.answer("Пожалуйста, выбери квест", reply_markup=keyboards.setting_quest_kb())
    await state.set_state(states.QuestsStates.setting_quest)


@router.message(Command("help"))
async def help_msg(msg: Message):
    await msg.answer(consts.get_help_message())


@router.message()
async def unknown_message(msg: Message):
    await msg.answer("Нет такого варианта!")


