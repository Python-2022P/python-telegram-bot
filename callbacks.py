from telegram.ext import CallbackContext
from telegram import Update


def echo_text(update: Update, context: CallbackContext):
    print(update.message.text)

def echo_photo(update: Update, context: CallbackContext):
    print(update.message.photo)