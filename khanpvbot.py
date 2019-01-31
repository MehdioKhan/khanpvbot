from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

token = '596158284:AAFwmTPZvls-quiACmSQVzE-bjSoxMJP4YM'
myChatID = 418419344


def start(bot, update):
    update.message.reply_text('سلام {}\n لطفا پیام خود را ارسال کنید'.format(
        update.message.from_user.first_name))


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def forwarder(bot, update):
    bot.forward_message(chat_id=myChatID, message_id=update.message.message_id,
                        from_chat_id=update.message.chat_id)


updater = Updater(token)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, forwarder))
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
