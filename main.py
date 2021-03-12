import os, discord
from dotenv import load_dotenv
from random import choice
from discord.ext import commands, tasks
from discord import *

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='.')

status = ['Jamming out to music!', 'Eating!', 'Sleeping!']

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == guild:
            break
    print(f'{client.user} has conected to {guild}!')


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     if message.content.startswith('hi'):  # za vise izbora mora 2 zagrade
#         await message.channel.send('Hello ' + str(message.author) + '!')

#     if message.content.startswith('reply'):
#         await message.reply("Hello I'm " + str(client.user))

#     if str(message.channel) == "general" and message.content != "":
#         await message.channel.purge(limit=1)


@client.command(name='linkk')
async def link(ctx):
    await ctx.send('https://discord.com/oauth2/authorize?client_id=812988652586139688&permissions=8&scope=bot')

@client.command(name='ping', help='This command returns the latency')
async def ping(ctx):
    await ctx.send(f'Latency: {round(client.latency * 1000)}ms')

@client.command(name='clear')
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@client.command(name='invite')
async def invite(ctx):
    """Create instant invite"""
    link = await ctx.channel.create_invite(max_age = 300)
    await ctx.send("Here is an instant invite to your server: " + link)


@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


client.run(TOKEN)