import discord
from random import choice
from discord.ext import tasks

from settings import *
import commands
commands

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print('------')
    print('Connected to:')
    for guild in client.guilds:
        print(guild.name)

    await client.change_presence(activity=status)


client.run(TOKEN)