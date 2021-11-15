from disnake.ext.commands import Converter
from disnake.ext.commands.core import is_nsfw

class LaTeXConverter(Converter):

    async def convert(self, ctx, arg : str):
        if not arg.startswith("$"):
            arg = "$" + arg
        
        if not arg.endswith("$"):
            arg = arg + "$"

        return arg