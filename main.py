import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Bot tokenini shu yerga yozing (BotFather'dan olgan tokeningiz)
API_TOKEN = '8448000665:AAHTQ_nmVUybAPUc_PtKj4T8rqY683Vzgq8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# /start komandasi uchun funksiya
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Salom! Bot muvaffaqiyatli ishga tushdi.")

# Botni ishga tushirish qismi
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
