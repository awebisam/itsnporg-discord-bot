import discord
from discord.ext import commands

class Links(commands.Cog):
    def __init__(self,client):
        self.client = client
    

    @commands.command()
    async def serverlink(self,ctx):
        link = 'https://discord.gg/gmzhmyZb8m'
        await ctx.send(link)
    
    @commands.command()
    async def grouplink(self,ctx):
        groupembed = discord.Embed(title="**The link of Facebook Group is**" ,description = "https://www.facebook.com/groups/techforimpact/",color=0x00ff00)
        await ctx.send(embed=groupembed)


def setup(client):
    client.add_cog(Links(client))