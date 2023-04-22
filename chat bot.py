import openai
from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API = os.getenv("OPENAI_API")
bot = Bot(token=BOT_TOKEN)  # username: @QuipsterBot
dp = Dispatcher(bot)


openai.api_key = OPENAI_API

def chatGPT(question):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content":f"{question}"}]
    )

    return completion.choices[0].message.content

@dp.message_handler(commands=['start'])
async def intro(message: types.Message):
    try:
        await message.answer(chatGPT('Hi'))
    except:
        pass

@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    try:
        await message.answer("""I am @QuipsterBot a Chat Bot integrated with ChatGPT.
Just type the topic which you want, i will answer you.
I can't answer the real time events7v.""")
    except:
        pass

@dp.message_handler()
async def echo(message: types.Message):
    try:
        await message.answer(chatGPT(message.text))
    except:
        pass


print("polling...")
executor.start_polling(dp)