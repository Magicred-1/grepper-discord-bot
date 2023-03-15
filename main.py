from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

load_dotenv() # Load the .env file

prefix = "!" # This is the default prefix
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(
    command_prefix=prefix,
    intents=discord.Intents.all(),
)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!\nBot latency : {round(bot.latency * 100, 2)}ms')

cogfiles = [
    f"cogs.{filename[:-3]}" for filename in os.listdir("./cogs/") if filename.endswith(".py")
]

for cogfile in cogfiles:
    try:
        bot.load_extension(cogfile)
    except Exception as err:
        print(err)

bot.run(token)