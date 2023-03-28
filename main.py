import telegram 
import os


TOKEN = os.environ.get('TOKEN')

bot = telegram.Bot(TOKEN)

print(bot.send_message('1258594598', 'ok'))
