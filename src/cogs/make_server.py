import discord
from discord.ext import commands 
from discord import app_commands
import datetime 
import logging
from roles_module import roles

bot = commands.Bot(command_prefix="<<", intents=discord.Intents.all())


class make(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name="make", description="Initalize the bot. This means that the bot will start making a server")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(agreement="Are you sure you want to start? YES/NO")
    
    async def make_server(self, interaction: discord.Interaction, agreement: str):
        
        guild = bot.fetch_guilds()
        
        if agreement == "yes":
            
            now = datetime.datetime.now()
            current_time = now.strftime('%H:%M:%S')

            try:
                with open('./cogs/happening.txt', 'r', encoding='utf-8') as file:
                    happening = file.read()

                intro_embed = discord.Embed(title="Information", description="**Your server is in the making ...**", url="https://discord.com/api/oauth2/authorize?client_id=1201924817607991297&permissions=8&scope=bot" , color=0x4169E1)
                intro_embed.add_field(name="What is happening now ?", value=f"{happening}", inline=False)
                intro_embed.set_footer(text=f"{current_time}" , icon_url="")
        

                await interaction.response.send_message(embed=intro_embed)

                try:
                    roles
                except Exception as rolesErr:
                    logging.warn(rolesErr)

            except Exception as makeErr:
                logging.warn(makeErr)

        else:
            await interaction.response.send_message("Not making any changes! Shuting down ...")

async def setup(bot):
    await bot.add_cog(make(bot))
    print("make cogs geladen ✔️")
