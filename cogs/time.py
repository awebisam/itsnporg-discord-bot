import discord 
from discord.ext import commands
from datetime import datetime
import pytz


class Time(commands.Cog):

    def __init__(self,client):
        self.client = client
    

    @commands.command()
    async def time(self,ctx,args):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            IST = pytz.timezone(str(args))
            datetime_ist = datetime.now(IST)
            time = datetime_ist.strftime("%I:%M %p")
            embed = discord.Embed(title=f'Hello {ctx.author} !',description=f'The Time in {args} is {time}')
            await ctx.send(embed=embed)
        
        else:
            await ctx.send(f'{ctx.author.mention} **,Use the bot-cmd channel to run the command!**',delete_after=10)


def setup(client):
    client.add_cog(Time(client))