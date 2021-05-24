import discord 
from discord.ext import commands
from nepse import NEPSE

try:
    init = NEPSE()
except:
    pass

class Nepse(commands.Cog):
    
    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def nepse(self,ctx,args):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            try:
                data = init.todayPrice(args)
                nepseembed = discord.Embed(title="NEPSE Data for {}".format(data["securityName"]),color=0xff0000)
                nepseembed.add_field(name="**Open Price**",value=data["openPrice"],inline=False)
                nepseembed.add_field(name="**Highest Price**",value=data["highPrice"],inline=False)
                nepseembed.add_field(name="**Lowest Price**",value=data["lowPrice"],inline=False)
                nepseembed.add_field(name="**Closing Price**",value=data["closePrice"],inline=False)
                nepseembed.add_field(name="**Last Updated Price**",value=data["lastUpdatedPrice"],inline=False)
                nepseembed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/rxvZr7oPFnT1PYp5DHluOA9a1F2d-wiUD-SgZ2LknZ8/https/cdn6.aptoide.com/imgs/a/8/4/a8435b6d8d3424dbc79a4ad52f976ad7_icon.png")
                nepseembed.set_footer(text="Business Date-{}".format(data["businessDate"]))
                await ctx.send(embed=nepseembed)
            except:
                await ctx.send("**API is down**")
        else:
            await ctx.send(f'{ctx.author.mention} **,Use the bot-cmd channel to run the command!**',delete_after=10)


def setup(client):
    client.add_cog(Nepse(client))