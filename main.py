import os
from discord.ext import commands
import discord
from settings import *

DISCORD_BOT_TOKEN = env_dict['DISCORD_BOT_TOKEN']

bot_id = DISCORD_BOT_TOKEN

activity = discord.Streaming(
    name=">help | Check out the bot with the url",
    url="https://github.com/Valiice/Howest-Discord-Bot",
)

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all(), activity=activity)


@bot.event
async def on_ready():
    print("{0.user} IS ONLINE.".format(bot))


for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")


bot.run(bot_id)
