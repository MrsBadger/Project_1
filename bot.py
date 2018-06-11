import telegram
from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import kernel

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет! Я могу подсказать тебе ближайшие электрички от Университета до Петербурга. Введи /sched.")

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Извини, я могу только присылать расписание. Нажми /help.")

def sched(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="Вот следующие электрички:\n" + '\n'.join(kernel.popSchedule()))

#основные вызовы
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
bot = telegram.Bot(token='618465775:AAHe5nrOVg0K8MHE8loVgTPOO-snCQ1mO7I')
updater = Updater(token='618465775:AAHe5nrOVg0K8MHE8loVgTPOO-snCQ1mO7I')
dispatcher = updater.dispatcher

#обработка /start
start_handler = CommandHandler('help', help)
dispatcher.add_handler(start_handler)
updater.start_polling()
#обработка /sched handler
sched_handler = CommandHandler('sched', sched)
dispatcher.add_handler(sched_handler)

#обработка неизвестных команд
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
