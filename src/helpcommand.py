import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

# https://gist.github.com/InterStellpassa0/b78488fb28cadf279dfd3164b9f0cf96

class MyHelp(commands.HelpCommand):
    #&help
    async def send_bot_help(self, mapping):
    ctx.send("This bot supports multiple commands. To find more about them just type ?Info{command}")
