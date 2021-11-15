from disnake import file
from disnake.app_commands import Option
from disnake.ext.commands.slash_core import slash_command
from sympy import init_printing
from sympy import Symbol, symbols, preview
import disnake
from disnake.ext import commands
from io import BytesIO
from utils.converters import LaTeXConverter

class MathCog(commands.Cog):
    def __init__(self, client : disnake.Client) -> None:

        self.client = client

    @commands.command(aliases=['tex'])
    async def latex(self, ctx, *, latex : LaTeXConverter):

        async with ctx.channel.typing(): # Jeopardy theme ensues...
            buffer = BytesIO()

            preview(
                latex,
                output='png',
                viewer="BytesIO",
                outputbuffer= buffer,
                euler=False,
                dvioptions=[
                    '-bg', 'rgb 0.0 0.0 0.0',
                    '-fg', 'rgb 1.0 1.0 1.0',
                    '-T', 'bbox',
                    '-z', '0',
                    '-x', '1440'
                ]
            )

            buffer.seek(0) # Going back to the beginning of the buffer so we can make a file out of that shit lol

            imageFile = disnake.File(buffer, filename="poggers.png")

            return await ctx.reply(
                "<:catThumbs:909593503821086750> **Rendered LaTeX**",
                file = imageFile
            )

def setup(client):
    init_printing()
    client.add_cog(MathCog(client))