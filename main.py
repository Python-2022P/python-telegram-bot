import telegram 
import os


TOKEN = os.environ.get('TOKEN')

bot = telegram.Bot(TOKEN)

updates = bot.get_updates()

print(updates[-1].message.text)
