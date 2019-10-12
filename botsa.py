from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url


def foo():
    text = " ".join(context.args)
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text='pohel na xyi ' + text,
    )
def get_image_url2():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url2()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def bop(bot, update):
    url = get_image_url()
    chat_id = update. message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
def bip(bot, update):
    url = get_image_url2()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('773684360:AAG1VJjcqo88AOlT9EAKpi05rvjVBR2tt3M')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('foo',foo))
    dp.add_handler(CommandHandler('sobaken',bop))
    dp.add_handler(CommandHandler('bip',bip))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()