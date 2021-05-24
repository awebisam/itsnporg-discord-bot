import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def ping(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            pingembed = discord.Embed(description = "Ping\n {}ms".format(int(self.client.latency*1000)))
            await ctx.send(embed=pingembed)
        
        else:
            await ctx.send(f'{ctx.author.mention} **,Use the bot-cmd channel to run the command!**',delete_after=10)
def setup(client):
    client.add_cog(Ping(client))