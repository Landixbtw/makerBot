import discord


class roles:
    def __init__(self, bot, guild):
        self.bot = bot
        self.guild = guild

    # Creating roles,
    # Add Colors
    async def create_roles(self):
        print("In Roles class")

        try:
            await self.guild.create_role(name="Administrator")
            await self.guild.create_role(name="Moderator")
            await self.guild.create_role(name="Supporter")
            await self.guild.create_role(name="[Server Team]")
            await self.guild.create_role(name="Bot")
            await self.guild.create_role(name="Server Friend")
            await self.guild.create_role(name="muted")
            await self.guild.create_role(name="community")
            await self.guild.create_role(name="age")
            await self.guild.create_role(name="20+")
            await self.guild.create_role(name="18+")
            await self.guild.create_role(name="16+")
            await self.guild.create_role(name="sex")
            await self.guild.create_role(name="male")
            await self.guild.create_role(name="female")
            # non binary
            await self.guild.create_role(name="language")
            await self.guild.create_role(name="english")
            await self.guild.create_role(name="german")
            await self.guild.create_role(name="french")
            await self.guild.create_role(name="england")
            await self.guild.create_role(name="Event Ping")

            print("Created roles")
        except Exception as createErr:
            print(f"Error creating roles: {createErr}")
