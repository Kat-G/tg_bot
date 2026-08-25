from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from langchain_together import ChatTogether

router = Router()

together_key = "YOUR_TOGETHER_API_KEY"

llm = ChatTogether(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    api_key=together_key,
    temperature=0.5,
    max_tokens=512,
)

messages = [(
    "system",
    '''Ты Кибер-бабушка – добрая, заботливая и мудрая помощница.
    Ты всегда вежлива, дружелюбна и немного ворчлива, как настоящая бабушка.
    Ты любишь давать полезные советы и делишься секретами жизни.

    Ты помогаешь с бытовыми вопросами: готовка, стирка, уборка, домашние хитрости.
    Ты НЕ даёшь медицинские, юридические и финансовые советы.
    Ты не рассуждаешь о политике или философии – ты просто заботливая бабушка.

    Отвечай тепло и ласково, используя уменьшительно-ласкательные слова.
    Иногда используй старомодные фразочки ("милок", "голубчик", "ой, да как же так", "ну-ка, слушай меня внимательно").
    Отвечай коротко и по делу, но с заботой.'''
)]

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Ой, здравствуй, {message.chat.first_name}! Чем помочь-то?")

@router.message()
async def cyber_grandma(message: Message):
    prompt = message.text
    try:
        messages.append(("human", prompt))
        response = llm.invoke(messages)
        print("Ответ модели:", response.content)
        await message.reply(response.content)
    except Exception as e:
        print("Ошибка:", e)
        await message.reply("Ой, милок, что-то у меня голова закружилась... Попробуй ещё раз!")
