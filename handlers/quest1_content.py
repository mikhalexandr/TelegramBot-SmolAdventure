from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import datetime
import keyboards
import consts


text = {


}


async def start_message(msg: Message, state: FSMContext):
    start = datetime.datetime.now()
    await state.update_data(start_time=start)
    await msg.answer("""Уважаемые гости!
    Добро пожаловать в увлекательную экскурсию по памятникам Смоленска, посвященным великой эпохе 1812 года! Сегодня мы отправимся в путешествие во времени, чтобы погрузиться в историю и открыть для себя места, связанные с этим важным периодом в истории России.
    В нашей экскурсии мы будем исследовать памятники, которые воздвигнуты в честь героической обороны Смоленска и подвигов, совершенных во время Отечественной войны 1812 года. Каждый из этих памятников является символом мужества, силы духа и патриотизма наших предков.
    """)
    await msg.answer("Для начала квеста придите к Монументу Защитникам Смоленска.", reply_markup=keyboards.done_kb())
    await msg.answer_sticker(consts.GUIDES_DICT["sis2hello"])
