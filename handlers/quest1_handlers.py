from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import datetime
import keyboards
from states import QuestsStates
import consts
import emoji
import db

sv1 = "AgACAgIAAxkBAAIb9WVPB57vdNmrFHe-KaRT1qgSsON-AAI1yjEb-qt5SiYZiIzqhf2QAQADAgADeQADMwQ"
sv2 = "AgACAgIAAxkBAAIb9mVPB8go56fkiJDznpXQorKyErfOAAI2yjEb-qt5So2kuLawAu4TAQADAgADeQADMwQ"

router = Router()


@router.message(QuestsStates.preparing_for_quest1, F.text == "Начать квест")
async def start_quest(msg: Message, state: FSMContext):
    await msg.answer("""Уважаемые гости!
Добро пожаловать в увлекательную экскурсию по памятникам Смоленска, посвященным великой эпохе 1812 года! Сегодня мы отправимся в путешествие во времени, чтобы погрузиться в историю и открыть для себя места, связанные с этим важным периодом в истории России.
В нашей экскурсии мы будем исследовать памятники, которые воздвигнуты в честь героической обороны Смоленска и подвигов, совершенных во время Отечественной войны 1812 года. Каждый из этих памятников является символом мужества, силы духа и патриотизма наших предков.
""")
    await msg.answer("Для начала квеста придите к Монументу Защитникам Смоленска", reply_markup=keyboards.done_kb())
    await state.update_data(start_time=datetime.datetime.now())
    await state.set_state(QuestsStates.task1_quest1_waiting)


@router.message(QuestsStates.task1_quest1_waiting, F.text == "Сделано!")
async def take_1_task(msg: Message, state: FSMContext):
    await msg.answer("""Приветствую, меня зовут Маргарита, и мне понадобится твоя помощь в изучении Отечественной войны 1812 года и роли Смоленска в ней. К счастью, я помню, что большую роль в сражении с Наполеоном сыграл великий русский полководец, чья ФАМИЛИЯ находится где-то на памятнике… 
Поможешь найти?""", reply_markup=keyboards.ReplyKeyboardRemove())
    await msg.answer_sticker(consts.GUIDES_DICT["sis2hello"])
    await state.update_data(tries=2)
    await state.set_state(QuestsStates.task1_quest1_answering)


@router.message(QuestsStates.task1_quest1_answering, F.text.lower() == "кутузов")
async def start_2_task(msg: Message, state: FSMContext):
    await msg.answer(
        """Это Михаил Илларионович Кутузов! К сожалению, он не может дать нам подсказку, ведь он живёт не в наше время. Однако может кто-то оставил его подсказки? Только вот где…? """)
    await msg.answer_sticker(consts.GUIDES_DICT["sis2true"])
    await msg.answer("""Давайте попробуем проверить около его бюста.
А пока вы будете идти до туда, я расскажу вам интересный факт, о котором вы, вероятно, когда-нибудь думали, но никогда не знали точного ответа:
Вы знали, что историю появления торта “Наполеон”, согласно одной из гигантского количества теорий, торт Наполеон, вообще не имеет никакого отношения к Франции. Дело в том, что к юбилею изгнания Наполеона из Москвы всегда готовилось большое количество разнообразных вкусностей, среди которых порой встречались самые настоящие кулинарные шедевры. Пир на весь мир как говорится. Именно так и появилось изначально слоеное пирожное, треугольной формы, обильно смазанное заварным кремом. Говорили, что форма символизирует треуголку Наполеона . А хруст коржей означал фиаско французов, и то, что нашей армии - все по зубам.""")
    await msg.answer("Идите на Аллею Героев!", reply_markup=keyboards.done_kb())
    await msg.answer_sticker(consts.GUIDES_DICT["sis2hm"])
    await state.set_state(QuestsStates.task2_quest1_waiting)


@router.message(QuestsStates.task1_quest1_answering)
async def incorrect_task_1(msg: Message, state: FSMContext):
    tries = (await state.get_data())["tries"]
    start_time = (await state.get_data())["start_time"]
    if not tries:
        await state.update_data(start_time=start_time - datetime.timedelta(minutes=10))
        await start_2_task(msg, state)
        return
    await state.update_data(tries=tries - 1)
    await state.update_data(start_time=start_time - datetime.timedelta(minutes=5))
    await msg.answer(f"Неверно! Попробуй ещё раз, у тебя осталось {tries} попытки(а)")
    await msg.answer_sticker(consts.GUIDES_DICT["sis2false"])


@router.message(QuestsStates.task2_quest1_waiting, F.text == "Сделано!")
async def take_2_task(msg: Message, state: FSMContext):
    await msg.answer_photo(sv1,
                           caption="""Итак, давайте поищем что-то на бюсте императора. Кажется, я что-то нашла! Это свиток, наверняка там есть какая-то подсказка… игра слов???""")
    await msg.answer("Напишите, о ком может идти речь? Может быть Кутузов смотрит на кого-то?...",
                     reply_markup=keyboards.ReplyKeyboardRemove())
    await msg.answer_sticker(consts.GUIDES_DICT["sis2hm"])
    await state.update_data(tries=2)
    await state.set_state(QuestsStates.task2_quest1_answering)


@router.message(QuestsStates.task2_quest1_answering, F.text.lower() == "дохтуров")
async def start_3_task(msg: Message, state: FSMContext):
    await msg.answer("Думаете Дохтуров? Точно! Это он!")
    await msg.answer_sticker(consts.GUIDES_DICT["sis2true"])
    await msg.answer(
        "А что за большой памятник недалеко? Это же «Благодарная Россия — Героям 1812 года»… Наверху я вижу двух орлов. Кстати, а на каких памятниках рядом еще изображены птицы, помню, что в названии монумента из белого камня было что-то связанно с именем София? Помогите мне вспомнить!")
    await msg.answer_sticker(consts.GUIDES_DICT["sis2hm"])
    await state.update_data(tries=2)
    await state.set_state(QuestsStates.task3_quest1_answering)


@router.message(QuestsStates.task2_quest1_answering)
async def incorrect_task_2(msg: Message, state: FSMContext):
    tries = (await state.get_data())["tries"]
    start_time = (await state.get_data())["start_time"]
    if not tries:
        await state.update_data(start_time=start_time - datetime.timedelta(minutes=10))
        await start_3_task(msg, state)
        return
    await state.update_data(tries=tries - 1)
    await state.update_data(start_time=start_time - datetime.timedelta(minutes=5))
    await msg.answer(f"Неверно! Попробуй ещё раз, у тебя осталось {tries} попытки(а)")
    await msg.answer_sticker(consts.GUIDES_DICT["sis2false"])


@router.message(QuestsStates.task3_quest1_answering, F.text.lower() == "памятник софийскому полку")
async def start_4_task(msg: Message, state: FSMContext):
    await msg.answer("Отлично, пойдёмте к этому памятнику!", reply_markup=keyboards.done_kb())
    await msg.answer_sticker(consts.GUIDES_DICT["sis2true"])
    await state.set_state(QuestsStates.task4_quest1_waiting)


@router.message(QuestsStates.task3_quest1_answering)
async def incorrect_task_3(msg: Message, state: FSMContext):
    tries = (await state.get_data())["tries"]
    start_time = (await state.get_data())["start_time"]
    if not tries:
        await state.update_data(start_time=start_time - datetime.timedelta(minutes=10))
        await msg.answer("Правильный ответ - памятник Софийскому полку!")
        await start_4_task(msg, state)
        return
    await state.update_data(tries=tries - 1)
    await state.update_data(start_time=start_time - datetime.timedelta(minutes=5))
    await msg.answer(f"Неверно! Попробуй ещё раз, у тебя осталось {tries} попытки(а)")
    await msg.answer_sticker(consts.GUIDES_DICT["sis2false"])


@router.message(QuestsStates.task4_quest1_waiting, F.text == "Сделано!")
async def take_4_task(msg: Message, state: FSMContext):
    await msg.answer_photo(sv2, caption="Я тут нашла ещё один свиток. На нем опять какое-то послание!")
    await msg.answer_sticker(consts.GUIDES_DICT["sis2hm"])
    await msg.answer("Идите к памятнику защитникам Смоленска 1812 года!")
    await state.set_state(QuestsStates.task4_quest1_answering)


@router.message(QuestsStates.task4_quest1_answering, F.text == "Сделано!")
async def end_quest(msg: Message, state: FSMContext):
    await msg.answer(
        """Вот и подошел к концу наш замечательный и увлекательный квест! Я очень рада была провести с вами время! Надеюсь, что вы узнали что-то новое! Вы можете пройти и другие квесты!""",
        reply_markup=keyboards.last_kb())
    start_time = (await state.get_data())["start_time"]
    await msg.answer(
        f"Ты потратил на квест {(datetime.datetime.now() - start_time).seconds / 60:.2f} минут (с учётом штрафного времени за ошибки) и заслужил подарок!",
        reply_markup=keyboards.get_stickers_kb())
    await msg.answer_sticker(consts.GUIDES_DICT["sis2true"])
    await state.set_state(QuestsStates.quest1_ending)
