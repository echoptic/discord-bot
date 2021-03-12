from settings import client
import discord

@client.command(name='link')
async def link(ctx):
    await ctx.send('https://discord.com/oauth2/authorize?client_id=812988652586139688&permissions=8&scope=bot')

@client.command(name='ping', help='This command returns the latency')
async def ping(ctx):
    await ctx.send(f'Latency: {round(client.latency * 1000)}ms')

@client.command(pass_context=True)
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    # await ctx.send(f'Nickname was changed for {member.mention} ')


#admin only commands
@client.command(name='klir')
async def clear(ctx, amount=2):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=amount)