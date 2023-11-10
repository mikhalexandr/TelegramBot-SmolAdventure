from aiogram import Router, F, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardMarkup
import consts

router = Router()


@router.message(Command("start"))
async def start(msg: Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="История Смоленска"),
        types.KeyboardButton(text="Квест"))
    global page
    page = 0
    await msg.answer(consts.START_MESSAGE,
                         reply_markup=builder.as_markup(resize_keyboard=True))


@router.message(Command("help"))
async def help(msg: Message):
    await msg.answer(consts.get_help_message())


@router.message(F.text == "История Смоленска")
async def smolhist(message: types.Message, page=0):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="1"), types.KeyboardButton(text="2")
    )
    builder.row(
        types.KeyboardButton(text="3"), types.KeyboardButton(text="4"),
        types.KeyboardButton(text="5"))
    builder.row(types.KeyboardButton(text="<="),
                types.KeyboardButton(text="=>"))
    await message.reply("Выберите материал", reply_markup=builder.as_markup(resize_keyboard=True))


@router.message(F.text == "Квест")
async def quest(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Экскурсия"), types.KeyboardButton(text=''))
    await message.reply("[текст экскурсии]", reply_markup=types.ReplyKeyboardRemove())
# @dp.message(Command("special_buttons"))
# async def cmd_special_buttons(message: types.Message):#     builder = ReplyKeyboardBuilder()
#     builder.row(#         types.KeyboardButton(text="Запросить геолокацию", request_location=True),
#         types.KeyboardButton(text="Запросить контакт", request_contact=True))#     await message.answer(
#         "Выберите действие:",#         reply_markup=builder.as_markup(resize_keyboard=True))
