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
    # get last message
    last_msg = current_update.message

    if last_update_id != current_update_id:
        # get text
        text = last_msg.text

        print(current_update_id, text)
        # send message
        last_msg.reply_text(text)

        last_update_id = current_update_id

    time.sleep(1)