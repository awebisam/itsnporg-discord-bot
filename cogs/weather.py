import discord
from discord.ext import commands
import json
import requests


class Weather(commands.Cog):

    def __init__(self,client):
        self.client = client
    

    @commands.command()
    async def weather(self,ctx,args):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            api_key = "de284bfa101c945598d61cbf30304249"     
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            complete_url = base_url + "appid=" + api_key + "&q=" + args
            response = requests.get(complete_url)
            data = response.json()
            main = data["main"]
            weather = data["weather"]
            city = data["name"] 
            temperature_in_celcius = int(main["temp"] - 273)
            embed = discord.Embed(title=f'Weather of {city}')
            embed.add_field(name="**Temperature**",value="{} °C".format(temperature_in_celcius),inline=False)
            embed.add_field(name="**Description**",value=str(weather[0]["description"]),inline=False)
            embed.set_thumbnail(url="https://i.pinimg.com/originals/06/c4/f7/06c4f70ec5931e2342e703e8a3f0a253.png")
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'{ctx.author.mention} **,Use the bot-cmd channel to run the command!**',delete_after=10)


def setup(client):
    client.add_cog(Weather(client))