import telegram 
import os


TOKEN = os.environ.get('TOKEN')

bot = telegram.Bot(TOKEN)

print(bot.getMe())
