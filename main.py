import telegram 
import os


TOKEN = os.environ.get('TOKEN')

bot = telegram.Bot(TOKEN)

updates = bot.get_updates()

last_update = updates[-1]

print(last_update.message.chat.id)
print(last_update.message.text)
