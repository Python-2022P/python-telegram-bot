import telegram 
import os
import time


TOKEN = os.environ.get('TOKEN')

bot = telegram.Bot(TOKEN)

while True:
    # get all updates
    updates = bot.get_updates()
    # last update
    last_update = updates[-1]
    # get last update id
    last_update_id = last_update.update_id
    # get update chat_id and text
    chat_id = last_update.message.chat.id
    text = last_update.message.text
    print(last_update_id, chat_id, text)
    bot.send_message(chat_id, text)

    time.sleep(1)