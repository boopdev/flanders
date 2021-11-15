import disnake
from disnake.ext import commands
from os import environ

class AcadiaBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        
        super().__init__(
            command_prefix='-',
            test_guilds = [909208958735110194, ],
            intents = disnake.Intents.all()
        )

        autoload_extensions = [
            'cogs.testCog',
            'cogs.mathCog'
        ]

        for ext in autoload_extensions:
            self.load_extension(ext)

if __name__ == "__main__":
    acadiaBotInstance = AcadiaBot()
    acadiaBotInstance.run(environ.get('BOT_TOKEN', None)) # We do a little environment variables

# ''