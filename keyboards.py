from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


def create_start_kb():
    kb = [KeyboardButton(text="История Смоленска"), KeyboardButton(text="Квесты")]
    return ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)
