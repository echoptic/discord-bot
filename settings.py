import os
from dotenv import load_dotenv
from discord.ext.commands import Bot
from discord import Game

#load bot token
load_dotenv()
TOKEN = os.getenv('TOKEN')

#change command prefix
client = Bot(command_prefix='.')

#change playing status
status = Game('zuri8')