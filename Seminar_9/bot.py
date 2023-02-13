import os
from dotenv import load_dotenv, find_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import logging

logging.basicConfig(filename='telebot.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


load_dotenv(find_dotenv())


def bot_quantity():
    global candies
    if candies > 28:
        candy = candies % 29
    else:
        candy = candies
    return candy


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}, работают команды:\n "/abc текст" - удаляет слова в которых присутствует словосочетание "абс"\n Игра в конфеты: для старта новой игры команда "/new_game",\n что бы сделать ход команда " /game "кол-во конфет"\n Наслаждайтесь ))) ')


async def new_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global candies
    candies = 100
    await update.message.reply_text(f'Вы начали новую игру, на столе {candies} конфет, можно брать не более 28 конфет за ход.')


async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global candies

    msg = update.message.text
    msg = msg.split()[1]
    msg_number = int(msg)
    candies -= msg_number
    await update.message.reply_text(f'Осталось  {candies} конфет')
    bot_candy = bot_quantity()
    await update.message.reply_text(f'Бот взял {bot_candy} конфет')
    candies -= bot_candy
    await update.message.reply_text(f'Осталось конфет {candies}')


async def abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    msg = filter(lambda x: 'абс' not in x, msg.split())
    my = " ".join(msg)
    await update.message.reply_text(my)

candies = 100

app = ApplicationBuilder().token(os.getenv('TOKEN')).build()

app.add_handler(CommandHandler("start", help))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help",  help))
app.add_handler(CommandHandler("abc", abc))
app.add_handler(CommandHandler("new_game", new_game))
app.add_handler(CommandHandler("game", game))
print('server start')
app.run_polling()
print('server stop')
