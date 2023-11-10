from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import keyboards
from states import HistoryStates
import consts

router = Router()


@router.message(HistoryStates.setting_history, F.text == "Назад")
async def escape_to_menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("Сделайте выбор...", reply_markup=keyboards.create_start_kb())


@router.message(HistoryStates.setting_history, F.text.in_(consts.HISTORIES))
async def setting_history(msg: Message, state: FSMContext):
    await state.update_data(history=msg)
    await msg.answer(f"Выбрано {msg.text}. Для начала нажмите Начать",
                     reply_markup=keyboards.preparing_for_history_kb())
    await state.set_state(HistoryStates.preparing_for_history)


@router.message(HistoryStates.preparing_for_history, F.text == "Назад")
async def escape_to_history_menu(msg: Message, state: FSMContext):
    await msg.answer("Пожалуйста, выбери предмет изучения", reply_markup=keyboards.setting_history_kb())
    await state.set_state(HistoryStates.setting_history)

