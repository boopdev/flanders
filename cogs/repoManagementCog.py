import disnake
from disnake.ext import commands
from utils import repoMan

class RepositoryManagementCog(commands.Cog):
    def __init__(self, client, *args, **kwargs) -> None:
        self.client = client

    @commands.slash_command(name='addrepo', description="Adds a repository for additional community modules.")
    async def addRepository(self, interaction, alias : str, url : str):
        pass

def setup(client):
    client.add_cog(
        RepositoryManagementCog(
            client = client
        )
    )