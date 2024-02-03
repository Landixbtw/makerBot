class deletion_roles:
    def __init__(self, dele_roles, guild):
        self.dele_roles = dele_roles
        self.guild = guild

    async def delroles(self):
        await self.dele_roles.delete()
