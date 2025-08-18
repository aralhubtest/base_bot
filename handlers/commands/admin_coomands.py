from aiogram import Router

from aiogram.filters import  Command
from aiogram.types import Message

router = Router()

@router.message(Command('admin'))
async def private(message: Message):
    await message.answer('Hello this is private')
