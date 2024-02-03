import discord
import time


class roles:
    def __init__(self, bot, guild):
        self.bot = bot
        self.guild = guild

    # Creating roles,
    # Add Colors

    async def create_roles(
        self,
    ):

        print("CREATING ROLES")

        try:
            await self.guild.create_role(name="Administrator")
            #           await ctx.send("Created role Administrator", ephemeral=True)
            time.sleep(1)
            await self.guild.create_role(name="Moderator")
            time.sleep(1)
            await self.guild.create_role(name="Supporter")
            time.sleep(1)
            await self.guild.create_role(name="[Server Team]")
            time.sleep(1)
            await self.guild.create_role(name="Bot")
            time.sleep(1)
            await self.guild.create_role(name="Server Friend")
            time.sleep(1)
            await self.guild.create_role(name="muted")
            time.sleep(1)
            await self.guild.create_role(name="community")
            time.sleep(1)
            await self.guild.create_role(name="age")
            time.sleep(1)
            await self.guild.create_role(name="20+")
            time.sleep(1)
            await self.guild.create_role(name="18+")
            time.sleep(1)
            await self.guild.create_role(name="16+")
            time.sleep(1)
            await self.guild.create_role(name="sex")
            time.sleep(1)
            await self.guild.create_role(name="male")
            time.sleep(1)
            await self.guild.create_role(name="female")
            time.sleep(1)
            # non binary
            await self.guild.create_role(name="language")
            time.sleep(1)
            await self.guild.create_role(name="english")
            time.sleep(1)
            await self.guild.create_role(name="german")
            time.sleep(1)
            await self.guild.create_role(name="french")
            time.sleep(1)
            await self.guild.create_role(name="england")
            time.sleep(1)
            await self.guild.create_role(name="Event Ping")

            print("Created roles")
        except Exception as createErr:
            print(f"Error creating roles: {createErr}")
