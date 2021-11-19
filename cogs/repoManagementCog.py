import disnake
from disnake.ext import commands
from utils import repoMan, buildingBlocks

class RepositoryManagementCog(commands.Cog):
    def __init__(self, client, *args, **kwargs) -> None:
        self.client = client
        self.repository_manager = repoMan.RepositoryManagementHelper('./repositories') # I hope this is where the docker volume is mounted

    #@commands.slash_command(name='listrepos', description="Lists all of the currently installed repositories.")
    @commands.command(name='listrepos')
    async def listRepositories(self, interaction):
        allRepos = self.repository_manager.getRepositoryList()
        repoConfigs = {i : self.repository_manager.getRepositoryConfig(i) for i in allRepos}

        for f, c in repoConfigs.items():
            print(f, c['name'], sep=" -> ")

    #@commands.slash_command(name='addrepo', description="Adds a repository for additional community modules.")
    @commands.command(name='addrepo')    
    async def addRepository(self, interaction, alias : str, url : str):
        
        async with interaction.channel.start_typing(): # Responsiveness

            self.repository_manager.cloneRepository(alias, url)
            config = self.repository_manager.getRepositoryConfig(alias)

            await interaction.channel.send(
                embed = buildingBlocks.Embed(
                    name = config['name'],
                    description = config['description']
                ).set_footer(
                    text = f"Author: {config['author']}",
                    icon_url = self.client.user.avatar_url
                ).set_author(
                    name = "Repository has been added!"
                )
            )

def setup(client):
    client.add_cog(
        RepositoryManagementCog(
            client = client
        )
    )