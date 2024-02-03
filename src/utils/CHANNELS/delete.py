import discord
import time


class delete_channels:
    def __init__(self, guild, channel):
        self.guild = guild
        self.channel = channel

    async def delete(self):

        await self.channel.delete()
