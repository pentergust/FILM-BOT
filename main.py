"""launching the bot"""

from config import BOT_TOKEN
from DoranimeBot import DoranimeBot

bot = DoranimeBot(BOT_TOKEN)
bot.run()
