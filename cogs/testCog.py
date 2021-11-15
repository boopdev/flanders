from disnake.ext.commands.slash_core import slash_command
import disnake
from disnake.ext import commands

class TestingCog(commands.Cog):
    def __init__(self, client : disnake.Client) -> None:
        self.client = client

    @commands.Cog.listener('ready')
    async def whenBotReady(self, *args, **kwargs):
        print("Flanders is running!")

    @slash_command(name="ping", description="Gets the bot latency")
    async def ping(self, inter):
        await inter.response.send_message(f"`🏓 Pong {round(self.client.latency * 500, 2)}ms`")

def setup(client):
    client.add_cog(TestingCog(client))