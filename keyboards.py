# клавиатуры

from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import consts


def create_start_kb():
    kb = [KeyboardButton(text="История Смоленска"), KeyboardButton(text="Квесты")]
    return ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)


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
