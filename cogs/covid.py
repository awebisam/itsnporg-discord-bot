import discord

from discord.ext import commands
import requests
import json

class Covid(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def covid(self,ctx,args):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            try:
                r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/{}'.format(args))
                data = json.loads(r.text)
                covidembed_1 = discord.Embed(title = "COVID-19 Stats {}".format(data['country']),color=0xff0000)
                covidembed_1.add_field(name="**Confirmed**",value=data["cases"],inline=False)
                covidembed_1.add_field(name="**Today's Cases**",value=data['todayCases'],inline=False)
                covidembed_1.add_field(name="**Deaths**",value=data["deaths"],inline=False)
                covidembed_1.add_field(name="**Today's Deaths**",value=data["todayDeaths"],inline=False)
                covidembed_1.add_field(name="**Recovered**",value=data["recovered"],inline=False)
                covidembed_1.add_field(name = "**Active Cases**",value=data["active"],inline=False)
                covidembed_1.set_thumbnail(url='http://www.ilovelibraries.org/sites/default/files/coronavirus-thumbnail.jpg')
                await ctx.send(embed = covidembed_1)
            except:
                await ctx.send("**API is down!**")
        else:
            await ctx.send(f'{ctx.author.mention} **,Use the bot-cmd channel to run the command!**',delete_after=10)


def setup(client):
    client.add_cog(Covid(client))
