import telegram 
import os
import time

def main():
    TOKEN = os.environ.get('TOKEN')

    bot = telegram.Bot(TOKEN)
    # for last update id
    last_update_id = -1
    while True:
        # current update
        curr_update = bot.get_updates()[-1]
        # current update id
        curr_update_id = curr_update.update_id
        # check new update
        if last_update_id != curr_update_id:
            last_message = curr_update.message
            # get data for send message
            chat_id = last_message.chat.id
            text = last_message.text
            if text:
                # send message
                bot.send_message(chat_id, text)

            last_update_id = curr_update_id
        
        time.sleep(1)


main()