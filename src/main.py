import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from datetime import datetime
import mariadb
import os
import logging
import sys
from helpcommand import MyHelp


load_dotenv()
token = str(os.getenv("TOKEN"))

# This handles the logging to a .log file
# So that it does not appear in the console output.
#
# logs_dir = "./logs/"
# if not os.path.exists(logs_dir):
#    print("Making the logs folder")
#    os.makedirs(logs_dir)
#    print("Made the logs folder")
## Logging handler
# handler = logging.FileHandler(filename="./logs/discord.log", encoding="utf-8", mode="w")

# This handles the "Bot" and a class for better organazation


class bot(commands.Bot):
    def __init__(
        self,
    ):
        super().__init__(command_prefix="<<", intents=discord.Intents.all())

    async def setup_hook(self):
        print("loading cogs ...")

        for file in os.listdir("./cogs/"):
            if file.endswith(".py"):
                try:
                    name = file[:-3]
                    await bot.load_extension(f"cogs.{name}")
                except Exception as cogsErr:
                    print(f"ERROR: {cogsErr}")

    async def on_ready(self):
        print(f"{bot.user.name} is ready to rumble!")
        print("Published by Moritz Henri Richard Reiswaffel III ")
        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} commands!")
        except Exception as syncErr:
            print(syncErr)

        print(f"discord version: {discord.__version__}")
        print("---------------------------")

        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name=f"{bot.command_prefix}help"
            )
        )


bot = bot()

bot.help_command = MyHelp()

bot.run(
    token,
)  # log_handler = handler
