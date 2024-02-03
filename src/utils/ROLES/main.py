import discord


class roles:
    def __init__(self, bot, guild):
        self.bot = bot
        self.guild = guild

    # Creating roles,
    # Add Colors
    async def create_roles(self, interaction: discord.Interaction):

        print("In Roles class")

        for guild in self.bot.guilds:
            await guild.create_role(name="Administrator")
            await guild.create_role(name="Moderator")
            await guild.create_role(name="Supporter")
            await guild.create_role(name="[Server Team]")
            await guild.create_role(name="Bot")
            await guild.create_role(name="Server Friend")
            await guild.create_role(name="muted")
            await guild.create_role(name="community")
            await guild.create_role(name="age")
            await guild.create_role(name="20+")
            await guild.create_role(name="18+")
            await guild.create_role(name="16+")
            await guild.create_role(name="sex")
            await guild.create_role(name="male")
            await guild.create_role(name="female")
            # non binary
            await guild.create_role(name="language")
            await guild.create_role(name="english")
            await guild.create_role(name="german")
            await guild.create_role(name="french")
            await guild.create_role(name="england")
            await guild.create_role(name="Event Ping")
