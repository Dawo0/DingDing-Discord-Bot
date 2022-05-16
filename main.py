import discord
from discord.ext import commands

description = "!post <name> <links>"
bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def post(ctx, name: str, *, links: str):
    '''takes name argument checks if channel exists and sends links to channel'''
    
    try:
        channel = discord.utils.get(ctx.guild.channels, name=name)
        channel_id = channel.id
        specific_write = bot.get_channel(channel_id)
        await specific_write.send(links)
    
    except:
        guild = ctx.guild
        cat = 'models'
        category = discord.utils.get(ctx.guild.categories, name=cat)
        create_channel = await guild.create_text_channel(name, category=category)
        channel = discord.utils.get(ctx.guild.channels, name=name)
        channel_id = channel.id
        specific_write = bot.get_channel(channel_id)
        await specific_write.send(links)

    await ctx.message.delete()


@bot.command()
async def say(ctx, *, msg: str):
    await ctx.send(msg)
    await ctx.message.delete()


bot.run("TOKEN")
