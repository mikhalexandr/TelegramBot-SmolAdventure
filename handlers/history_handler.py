from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import keyboards
from states import HistoryStates
import consts
from handlers.history_handlers import history1, history2, history3

router = Router()
router.include_routers(history1.router, history2.router, history3.router)


@router.message(HistoryStates.setting_history, F.text == "Назад")
async def escape_to_menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("Сделайте выбор...", reply_markup=keyboards.create_start_kb())


@router.message(HistoryStates.setting_history, F.text.in_(consts.HISTORIES))
async def setting_history(msg: Message, state: FSMContext):
    num = consts.HISTORIES.index(msg.text) + 1
    await state.update_data(history=num)
    await msg.answer(f"Выбрано {msg.text}. Для начала нажмите Начать",
                     reply_markup=keyboards.preparing_for_history_kb())
    await state.set_state(HistoryStates.preparing_for_history)


@router.message(HistoryStates.preparing_for_history, F.text == "Начать")
async def start_history(msg: Message, state: FSMContext):
    await state.set_state(eval(f"HistoryStates.history{(await state.get_data())['history']}_passing"))


@router.message(HistoryStates.preparing_for_history, F.text == "Назад")
async def escape_to_history_menu(msg: Message, state: FSMContext):
    await msg.answer("Пожалуйста, выбери предмет изучения", reply_markup=keyboards.setting_history_kb())
    await state.set_state(HistoryStates.setting_history)

