from typing import clear_overloads
import discord
from discord.ext import commands
from discord import ExpireBehavior, IntegrationAccount, app_commands, guild, message
import datetime
import logging
import time


from utils.ROLES.main import roles


bot = commands.Bot(command_prefix="<<", intents=discord.Intents.all())


class make(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="make",
        description="Initalize the bot. !!The Bot will delete every Channel and Role it can.!!",
    )
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(agreement="Are you sure you want to start? yes/no")
    async def make_server(
        self,
        interaction: discord.Interaction,
        agreement: str,
    ):
        Iguild = interaction.guild
        dev_server_link = "[discord server](<https://discord.gg/Ryd5uz7J2n>)"
        report_issue_here = "[here](<https://discord.gg/Ryd5uz7J2n>)"
        if agreement == "yes":
            # now = datetime.datetime.now()
            # current_time = now.strftime("%H:%M:%S")

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
                    name="What is happening now ?", value=f"{happening}", inline=False
                )
                # intro_embed.set_footer(text=f"{current_time}", icon_url="")

                await interaction.response.send_message(embed=intro_embed)

                async def roles_channel():
                    for x in interaction.guild.roles:
                        try:
                            await x.delete()
                            await interaction.response.send_message(
                                "I am cleaning up the server ... Removing all roles."
                            )

                        except Exception as roledeleteErr:
                            print("Error while deleting all roles.")
                            await interaction.response.send_message(
                                f"ERROR CODE 1: --> {roledeleteErr}\n Please report this to the maintainer {report_issue_here} \n Bot cant delete role.",
                                ephemeral=True,  # ERROR CODE 1 Error while deleting roles
                            )
                            logging.warn(roledeleteErr)

                        # TODO: Check ob kein CHannel mehr da, dann alle Channel erstellen

                        if len(interaction.guild.channels) == 0:
                            return
                        else:
                            for c in interaction.guild.channels:
                                try:
                                    await c.delete()
                                    await interaction.followup.send()

                                except Exception as channeldeleteErr:
                                    print(
                                        f"Bot exit with ERROR CODE 2: --> {channeldeleteErr} \n Please report this to the maintainer. https://discord.gg/Ryd5uz7J2n"  # ERROR CODE 2 Error while deleting channels
                                    )

                # TODO: Checken das macher-logs nicht gelöscht wird.

                try:
                    try:
                        await interaction.guild.create_text_channel(name="macher-logs")
                    except Exception as macher_logs_create_Err:
                        print(f"macher_logs setup ERROR: {macher_logs_create_Err}")
                        await interaction.response.send_message(
                            f"ERROR CODE 3: --> {macher_logs_create_Err} \n Please report this to the maintainer {report_issue_here} \n Bot cant create channel",
                            ephemeral=True,  # ERROR CODE 3 Error while making the macher-logs channel
                        )
                    # TODO: Create permissions and colors for the roles.
                    await roles_channel()
                    my_roles = roles(bot, Iguild)
                    await my_roles.create_roles()
                    await interaction.response.send_message(f"Created role {roles}")
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
