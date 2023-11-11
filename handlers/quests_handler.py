# обработчики для выбора квеста

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import datetime
import keyboards
from states import QuestsStates
import consts
import db

router = Router()


@router.message(QuestsStates.setting_quest, F.text == "Назад")
async def escape_to_menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("Сделайте выбор...", reply_markup=keyboards.create_start_kb())


@router.message(QuestsStates.setting_quest, F.text.in_(consts.QUESTS))
async def setting_quest(msg: Message, state: FSMContext):
    num = consts.QUESTS.index(msg.text) + 1
    await state.update_data(quest=num)
    await msg.answer(f"Выбран квест {msg.text}! Теперь присоединись к команде или создай новую",
                     reply_markup=keyboards.set_team_kb())
    await state.set_state(QuestsStates.setting_team)


@router.message(QuestsStates.adding_to_team, F.text == "Назад")
@router.message(QuestsStates.creating_team_name, F.text == "Назад")
async def return_to_team_menu(msg: Message, state: FSMContext):
    await msg.answer(
        f"Выбран квест {consts.QUESTS[(await state.get_data())['quest'] - 1]}! Теперь присоединись к команде или создай новую",
        reply_markup=keyboards.set_team_kb())
    await state.set_state(QuestsStates.setting_team)


@router.message(QuestsStates.setting_team, F.text == "Создать команду")
async def create_team(msg: Message, state: FSMContext):
    await state.set_state(QuestsStates.creating_team_name)
    await msg.answer("Пожалуйста, введи имя своей команды", reply_markup=keyboards.escape_kb())


@router.message(QuestsStates.creating_team_name)
async def create_team_and_prepare(msg: Message, state: FSMContext):
    if not db.create_team(msg.text):
        await msg.answer("К сожалению, такая команда уже сушествует! Пожалуйста, введи другое имя")
    else:
        db.add_team_member(msg.from_user.id, msg.from_user.username, msg.text)
        await state.set_state(QuestsStates.preparing_for_quest)
        await msg.answer(
            f"Команда {msg.text} успешно создана! Для начала приключения нажми Начать квест",
            reply_markup=keyboards.preparing_for_quest_kb())


@router.message(QuestsStates.setting_team, F.text == "Присоединиться к команде")
async def add_to_team(msg: Message, state: FSMContext):
    await state.set_state(QuestsStates.adding_to_team)
    await msg.answer("Пожалуйста, введи имя команды, к которой хочешь присоединиться",
                     reply_markup=keyboards.escape_kb())


@router.message(QuestsStates.adding_to_team)
async def add_to_team_and_prepare(msg: Message, state: FSMContext):
    if not db.add_team_member(msg.from_user.id, msg.from_user.username, msg.text):
        await msg.answer(
            "К сожалению, такой команды не существует. Пожалуйста, введи уже сущетсвующую команду или создай новую")
    else:
        await state.set_state(QuestsStates.preparing_for_quest)
        await msg.answer(f"Ты успешно присоединился к команде {msg.text}. Нажми Начать квест, чтобы начать квест",
                         reply_markup=keyboards.preparing_for_quest_kb())


@router.message(QuestsStates.setting_team, F.text == "Назад")
async def escape_to_team_menu(msg: Message, state: FSMContext):
    await msg.answer("Пожалуйста, выбери квест", reply_markup=keyboards.setting_quest_kb())
    await state.set_state(QuestsStates.setting_quest)


@router.message(QuestsStates.preparing_for_quest, F.text == "Начать квест")
async def start_quest(msg: Message, state: FSMContext):
    start = datetime.datetime.now()
    await state.update_data(start_time=start)
    await msg.answer("""Уважаемые гости!
Добро пожаловать в увлекательную экскурсию по памятникам Смоленска, посвященным великой эпохе 1812 года! Сегодня мы отправимся в путешествие во времени, чтобы погрузиться в историю и открыть для себя места, связанные с этим важным периодом в истории России.
В нашей экскурсии мы будем исследовать памятники, которые воздвигнуты в честь героической обороны Смоленска и подвигов, совершенных во время Отечественной войны 1812 года. Каждый из этих памятников является символом мужества, силы духа и патриотизма наших предков.
""")
    await msg.answer("Для начала квеста придите к Монументу Защитникам Смоленска.", reply_markup=keyboards.done_kb())
    await msg.answer_sticker(consts.GUIDES_DICT["sis2hello"])
    await state.set_state(QuestsStates.reading_quest)
