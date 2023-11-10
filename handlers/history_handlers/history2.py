# обработчики для проведения экскурсии 2

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import HistoryStates
import keyboards

router = Router()


@router.message(HistoryStates.history2_passing, F.text == "Далее")
async def next_information(msg: Message, state: FSMContext):
    try:
        text = (await state.get_data())["text"]
        await msg.answer(next(text), reply_markup=keyboards.next_kb())
    except StopIteration:
        await msg.answer("Рассказ завершен. Пожалуйста, пройди тест!")