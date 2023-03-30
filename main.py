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
                
            photo = last_message.photo
            if photo:
                #send photo
                bot.send_photo(chat_id, photo[-1])
                
            video = last_message.video
            if video:
                #send video
                bot.send_video(chat_id, video)
            
            contact = last_message.contact
            if contact:
                #send contact
                bot.send_contact(chat_id, contact.phone_number, contact.first_name, contact.last_name)
            
            location = last_message.location
            if location:
                #send location
                bot.send_location(chat_id, location.latitude, location.longitude)
            last_update_id = curr_update_id
            
            sticker = last_message.sticker
            if sticker:
                #send sticker
                bot.send_sticker(chat_id, sticker)
                
            voice = last_message.voice
            if voice:
                #send voice
                bot.send_voice(chat_id, voice)
            
            audio = last_message.audio
            if audio:
                #send audio
                bot.send_audio(chat_id, audio)
                
            dice = last_message.dice
            if dice:
                #send dice
                bot.send_dice(chat_id, dice.emoji)
                
            # poll = last_message.poll
            # if poll:
            #     #send poll 
            #     bot.send_poll(chat_id, poll.id)
                
        
        time.sleep(1)


main()