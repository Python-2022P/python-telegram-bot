import os
from telegram.ext import Updater, MessageHandler, Filters

from callbacks import (
    echo_photo,
    echo_text
)

TOKEN = os.environ.get('TOKEN')


# updater
updater = Updater(TOKEN)
# dispatcher
dispatcher = updater.dispatcher

dispatcher.add_handler(handler=MessageHandler(filters=Filters.text, callback=echo_text))
dispatcher.add_handler(handler=MessageHandler(filters=Filters.photo, callback=echo_photo))

updater.start_polling()
updater.idle()