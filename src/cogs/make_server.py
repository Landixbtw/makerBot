from typing import clear_overloads
import discord
from discord.ext import commands
from discord import app_commands
import datetime
import logging


from utils.ROLES.main import roles
from utils.ROLES.delete_roles import deletion_roles 
from utils.CHANNELS.delete import delete_channels


bot = commands.Bot(command_prefix="<<", intents=discord.Intents.all())


class make(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="make",
        description="Initalize the bot. !!The Bot will delete every Channel and Roles.!!",
    )
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(agreement="Are you sure you want to start? yes/no")
    async def make_server(self, interaction: discord.Interaction, agreement: str):

        guild = interaction.guild

        if agreement == "yes":

            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")

            try:
                with open("./cogs/happening.txt", "r", encoding="utf-8") as file:
                    happening = file.read()

                intro_embed = discord.Embed(
                    title="Information",
                    description="**Your server is in the making ...**",
                    url="https://discord.com/api/oauth2/authorize?client_id=1201924817607991297&permissions=8&scope=bot",
                    color=0x4169E1,
                )
                intro_embed.add_field(
                    name="What is happening now ?",https://github.com/kry0sc0pic/Raider/tree/master value=f"{happening}", inline=False
                )
                intro_embed.set_footer(text=f"{current_time}", icon_url="")

                await interaction.response.send_message(embed=intro_embed)

                try:
                    clear_roles = roles_delete(roles, guild)
                    await clear_roles.delete_roles()
                    pass
                except Exception as deleteErr:
                    print("Error while deleting all channels and roles.")
                    logging.warn(deleteErr)

                try:
                    my_roles = roles(bot, guild)
                    await my_roles.create_roles()
                except Exception as rolesErr:
                    logging.warn(rolesErr)

            except Exception as makeErr:
                logging.warn(makeErr)

        else:
            await interaction.response.send_message(
                "Not making any changes! Shuting down ..."
            )


async def setup(bot):
    await bot.add_cog(make(bot))
    print("make cogs geladen ✔️")
