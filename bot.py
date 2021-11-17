import disnake
from disnake.ext import commands
from os import environ
from asyncpg import create_pool

class AcadiaBot(commands.Bot):
    def __init__(self, *args, **kwargs):

        self.db = None
        self.loop.run_until_complete(self.init_database())
        
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


    async def init_database(self, *args, **kwargs) -> None:
        """Initializes the database connection pool

        """
        
        self.db = await create_pool(
            database = environ.get("DB_NAME"),
            username = environ.get("DB_USERNAME"),
            password = environ.get("DB_PASSWORD")
        )

        await self.run_database_schema()

    async def run_database_schema(self, *args, **kwargs) -> None:
        """Runs inital queries to setup the database
        """

        with open("./schema.sql", 'r', encoding='utf-8') as schema:
            await self.db.execute(schema.read())

        return

if __name__ == "__main__":
    acadiaBotInstance = AcadiaBot()
    acadiaBotInstance.run(environ.get('BOT_TOKEN', None)) # We do a little environment variables
