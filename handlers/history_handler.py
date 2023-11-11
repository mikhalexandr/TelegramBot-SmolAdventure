# обработчики для выбора истории

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import keyboards
from states import HistoryStates
import consts
import emoji
from handlers.history_texts import *
from handlers.history_images import *

router = Router()


@router.message(HistoryStates.quiz_ending, F.text == "Завершить!")
@router.message(HistoryStates.setting_history, F.text == "Назад")
async def escape_to_menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("Сделайте выбор...", reply_markup=keyboards.create_start_kb())


@router.message(HistoryStates.setting_history, F.text.in_(consts.HISTORIES))
async def setting_history(msg: Message, state: FSMContext):
    num = consts.HISTORIES.index(msg.text) + 1
    await state.update_data(history=num)
    await msg.answer(f"Выбрано: {msg.text}. Для старта нажмите Начать",
                     reply_markup=keyboards.preparing_for_history_kb())
    await state.set_state(HistoryStates.preparing_for_history)


@router.message(HistoryStates.preparing_for_history, F.text == "Начать")
async def start_history(msg: Message, state: FSMContext):
    num = (await state.get_data())['history']
    await state.set_state(HistoryStates.history_passing)
    await state.update_data(text=iter(eval(f"text{num}")), imgs=iter(eval(f"images{num}")))
    await next_information(msg, state)


@router.message(HistoryStates.history_passing, F.text == "Далее")
async def next_information(msg: Message, state: FSMContext):
    try:
        text = (await state.get_data())["text"]
        imgs = (await state.get_data())["imgs"]
        img = next(imgs)
        if not img:
            await msg.answer(next(text), reply_markup=keyboards.next_kb())
        else:
            await msg.answer_photo(img, caption=next(text), reply_markup=keyboards.next_kb())
    except StopIteration:
        await msg.answer("Рассказ завершен. Пожалуйста, пройди тест!", reply_markup=keyboards.lets_go_kb())
        await msg.answer_sticker(consts.GUIDES_DICT["sis1hm"])
        await state.set_state(HistoryStates.quiz_passing_preparing)


@router.message(HistoryStates.preparing_for_history, F.text == "Назад")
async def escape_to_history_menu(msg: Message, state: FSMContext):
    await msg.answer("Привет-привет, я Катя, пожалуйста, выбери нашего земляка, о котором хочешь узнать побольше!",
                     reply_markup=keyboards.setting_history_kb())
    await msg.answer_sticker(consts.GUIDES_DICT["sis1hello"])
    await state.set_state(HistoryStates.setting_history)


@router.message(HistoryStates.quiz_passing_preparing, F.text == "Вперёд!")
async def start_quiz(msg: Message, state: FSMContext):
    num = (await state.get_data())['history']
    await state.set_state(HistoryStates.quiz_passing)
    await state.update_data(quiz=iter(eval(f"quiz{num}")), answers=[])
    await next_quiz_question(msg, state)


async def next_quiz_question(msg: Message, state: FSMContext):
    try:
        quiz = (await state.get_data())["quiz"]
        question = next(quiz)
        answers = eval(f"quiz{(await state.get_data())['history']}")[question]
        right = answers[4]
        text = f"{question}\n{'A. ' + answers[0]}\n{'B. ' + answers[1]}\n{'C. ' + answers[2]}\n{'D. ' + answers[3]}"
        await state.update_data(answer=right)
        await msg.answer(text, reply_markup=keyboards.answer_quiz_kb())
    except StopIteration:
        text = "Результат:\n"
        score = 0
        for right, usr in (await state.get_data())['answers']:
            if right == usr:
                s = emoji.emojize(":check_mark_button:")
                score += 1
            else:
                s = emoji.emojize(":cross_mark:")
            s += f"  Ваш ответ:  {usr}  |  правильный ответ:  {right}\n"
            text += s
        text = text[:10] + f" {score * 10}%" + text[10:]
        await msg.answer(text, reply_markup=keyboards.last_kb())
        await msg.answer_sticker(consts.GUIDES_DICT["sis1true"] if score > 5 else consts.GUIDES_DICT["sis1false"])
        await state.set_state(HistoryStates.quiz_ending)


@router.message(HistoryStates.quiz_passing, F.text.in_(("A", "B", "C", "D")))
async def check_answer(msg: Message, state: FSMContext):
    ans = (await state.get_data())['answer']
    sp = (await state.get_data())['answers']
    sp.append((ans, msg.text))
    await state.update_data(answers=sp)
    await next_quiz_question(msg, state)
