from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import consts

router = Router()


@router.message(Command("start"))
async def start(msg: Message):
    await msg.answer(consts.START_MESSAGE)

