# обработчики для выбора истории

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import keyboards
from states import HistoryStates
import consts
from handlers.history_texts import *

router = Router()


@router.message(HistoryStates.setting_history, F.text == "Назад")
async def escape_to_menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("Сделайте выбор...", reply_markup=keyboards.create_start_kb())


@router.message(HistoryStates.setting_history, F.text.in_(consts.HISTORIES))
async def setting_history(msg: Message, state: FSMContext):
    num = consts.HISTORIES.index(msg.text) + 1
    await state.update_data(history=num)
    await msg.answer(f"Выбрано {msg.text}. Для старта нажмите Начать",
                     reply_markup=keyboards.preparing_for_history_kb())
    await state.set_state(HistoryStates.preparing_for_history)


@router.message(HistoryStates.preparing_for_history, F.text == "Начать")
async def start_history(msg: Message, state: FSMContext):
    num = (await state.get_data())['history']
    await state.set_state(HistoryStates.history_passing)
    await state.update_data(text=iter(eval(f"text{num}")))
    await next_information(msg, state)


@router.message(HistoryStates.history_passing, F.text == "Далее")
async def next_information(msg: Message, state: FSMContext):
    try:
        text = (await state.get_data())["text"]
        await msg.answer(next(text), reply_markup=keyboards.next_kb())
    except StopIteration:
        await msg.answer("Рассказ завершен. Пожалуйста, пройди тест!", reply_markup=keyboards.lets_go_kb())
        await state.set_state(HistoryStates.quiz_passing_preparing)


@router.message(HistoryStates.preparing_for_history, F.text == "Назад")
async def escape_to_history_menu(msg: Message, state: FSMContext):
    await msg.answer("Пожалуйста, выбери предмет изучения", reply_markup=keyboards.setting_history_kb())
    await state.set_state(HistoryStates.setting_history)


@router.message(HistoryStates.quiz_passing_preparing, F.text == "Вперёд!")
async def start_quiz(msg: Message, state: FSMContext):
    num = (await state.get_data())['history']
    await state.set_state(HistoryStates.quiz_passing)
    await state.update_data(quiz=iter(eval(f"quiz{num}")))
    await next_quiz_question(msg, state)


async def next_quiz_question(msg: Message, state: FSMContext):
    try:
        quiz = (await state.get_data())["quiz"]
        question = next(quiz)
        answers = eval(f"quiz{(await state.get_data())['history']}")[question]
        right = answers[4]
        text = f"{question}\n{'a. ' + answers[0]}\n{'б. ' + answers[1]}\n{'в. ' + answers[2]}\n{'г. ' + answers[3]}"
        await state.update_data(answer=right)
        await msg.answer(text, reply_markup=keyboards.answer_quiz_kb())
    except StopIteration:
        await msg.answer("Результат")


@router.message(HistoryStates.quiz_passing, F.text.in_(("а", "б", "в", "г")))
async def check_answer(msg: Message, state: FSMContext):
    if msg.text == (await state.get_data())['answer']:
        await msg.answer("Правильно!")
    else:
        await msg.answer(f"Неверно! Правильный ответ: {(await state.get_data())['answer']}")
    await next_quiz_question(msg, state)
