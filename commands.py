from settings import client

@client.command(name='link')
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