import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello there!")

@bot.event
async def on_message(message):
    if 'shit' in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, please refrain from using inappropriate language.")
    await bot.process_commands(message)


with open("token.txt") as f:
    token = f.read()

bot.run(token)
