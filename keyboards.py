# клавиатуры

from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import consts
import emoji


def create_start_kb():
    kb = [[KeyboardButton(text="История Смоленска"), KeyboardButton(text="Квесты")],
          [KeyboardButton(text="Поддержать автора")]]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def setting_quest_kb():
    builder = ReplyKeyboardBuilder()
    for i in consts.QUESTS:
        builder.add(KeyboardButton(text=i))
    builder.adjust(3)
    builder.row(KeyboardButton(text="Назад"))
    return builder.as_markup(resize_keyboard=True)


def setting_history_kb():
    builder = ReplyKeyboardBuilder()
    for i in consts.HISTORIES:
        builder.add(KeyboardButton(text=i))
    builder.adjust(3)
    builder.row(KeyboardButton(text="Назад"))
    return builder.as_markup(resize_keyboard=True)


def set_team_kb():
    kb = [[KeyboardButton(text="Создать команду"), KeyboardButton(text="Присоединиться к команде")],
          [KeyboardButton(text="Назад")]]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def preparing_for_quest_kb():
    kb = [KeyboardButton(text="Начать квест")]
    return ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)


def preparing_for_history_kb():
    kb = [[KeyboardButton(text="Начать")], [KeyboardButton(text="Назад")]]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def next_kb():
    kb = [KeyboardButton(text="Далее")]
    return ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)


def lets_go_kb():
    kb = [KeyboardButton(text="Вперёд!")]
    return ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)


def answer_quiz_kb():
    builder = ReplyKeyboardBuilder()
    for i in "ABCD":
        builder.add(KeyboardButton(text=i))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def last_kb():
    kb = [KeyboardButton(text="Завершить!")]
    return ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)


def escape_kb():
    kb = [KeyboardButton(text="Назад")]
    return ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)


def done_kb():
    kb = [KeyboardButton(text="Сделано!")]
    return ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)


def get_stickers_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="emoji.emojize(':check_mark_button:') Забрать подарок emoji.emojize("
                                          "':check_mark_button:')", url="https://t.me/addstickers/Smolensks"))
    return builder.as_markup()


def payments_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Поддержать автора",
                                     url="https://www.sberbank.com/sms/pbpn?requisiteNumber=79525302125"))
    return builder.as_markup()
