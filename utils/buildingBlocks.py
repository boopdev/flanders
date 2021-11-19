import disnake

class Embed(disnake.Embed):
    def __init__(self, *args, **kwargs):
        kwargs['colour'] =  kwargs.pop('colour', 0x9A2A2A) # Default colour
        super().__init__(self, *args, **kwargs)
