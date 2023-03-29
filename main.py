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
    #get user chat_id
    chat_id = current_update.message.chat_id
    # get current update id
    current_update_id = current_update.update_id
    # get last message
    last_msg = current_update.message

    if last_update_id != current_update_id:
        # get text
        text = last_msg.text
        sticker = last_msg.sticker
        photo = last_msg.photo
        video = last_msg.video
        cantact = last_msg.contact
        lacation = last_msg.location
        voice = last_msg.voice
        audio = last_msg.audio
        dice = last_msg.dice
        poll=last_msg.poll
        print(poll.options[-1])
        
        if text:
            bot.send_message(chat_id,text)
        elif photo:
            bot.send_photo(chat_id,photo[-1].file_id)
        elif sticker:
            bot.send_sticker(chat_id,sticker)
        elif video:
            bot.send_video(chat_id,video)
        elif cantact:
            bot.send_contact(chat_id,cantact.phone_number,cantact.first_name,cantact.last_name,cantact.vcard)
        elif lacation:
            bot.send_location(chat_id,lacation.latitude,lacation.longitude)
        elif voice:
            bot.send_voice(chat_id,voice.file_id)
        elif audio:
            bot.send_audio(chat_id,audio.file_id)
        elif dice:
            bot.send_dice(chat_id,dice.emoji)
        elif poll:
            option = []
            for i in poll.options:
                option.append(i["text"])
                print(i)
                
            bot.send_poll(chat_id,poll.question,option)
        


        last_update_id = current_update_id

    time.sleep(1)