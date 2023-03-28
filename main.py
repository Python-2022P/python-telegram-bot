import telegram 
import os
import time


TOKEN = os.environ.get('TOKEN')
bot = telegram.Bot(TOKEN)

# default update id
last_update_id = -1
while True:
    # get all updates
    updates = bot.get_updates()
    # current update
    current_update = updates[-1]
    # get current update id
    current_update_id = current_update.update_id
    # get update chat_id and text
    chat_id = current_update.message.chat.id
    text = current_update.message.text

    if last_update_id != current_update_id:
        print(current_update_id, chat_id, text)
        bot.send_message(chat_id, text)

        last_update_id = current_update_id

    time.sleep(1)