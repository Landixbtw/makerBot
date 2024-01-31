import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='<<', intents=intents)

# https://gist.github.com/InterStellpassa0/b78488fb28cadf279dfd3164b9f0cf96

class MyHelp(commands.HelpCommand):
    #&help
    async def send_bot_help(self, mapping ):
        await self.context.send("This bot supports one command, the **/make** command. This will 'make' the server. If you have any questions join here and tag me ill be happy to answer:  https://discord.gg/Ryd5uz7J2n ")
