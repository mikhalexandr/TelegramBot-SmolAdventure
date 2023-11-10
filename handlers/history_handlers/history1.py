# обработчики для проведения экскурсии 1

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import HistoryStates
import keyboards
from handlers.history_handlers.texts import text1

router = Router()


@router.message(HistoryStates.history1_passing, F.text == "Далее")
async def next_information(msg: Message, state: FSMContext):
    try:
        await msg.answer(next(text1), reply_markup=keyboards.next_kb())
    except StopIteration:
        await msg.answer("Рассказ завершен. Пожалуйста, пройди тест!")

