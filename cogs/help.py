import discord
from discord.ext import commands
import json
from discord.utils import get

with open('muted_history.json', encoding='utf-8') as f:
  try:
    muted = json.load(f)
  except ValueError:
    muted = {}
    muted['users'] = []

class Help(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity = discord.Game('Minecraft'))
        print("Bot is Ready!")

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.client.get_channel(834623259458404412)
        embed = discord.Embed(title="Welcome to IT Students of Nepal!",description=f'Hello {member.mention}!!\nEnjoy your stay here :heart:\nGet yourself some roles from <#845556023637049384> \nRead our Server Rules <#833995240905113640>\nIntroduce yourself in <#834001977063112715>\nGreetings!!')
        embed.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed)
        
        with open('muted_history.json', encoding='utf-8') as f:
            try:
                muted = json.load(f)
            except ValueError:
                muted = {}
                muted['users'] = []

        role = discord.utils.get(member.guild.roles,name="Muted")
        newlist = filter(lambda x : len(x)>0 , muted["users"])
        for current_user in newlist:
            if member.name == current_user['name']:
                await member.add_roles(role)


    
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        errors = str(error)
        embed = discord.Embed(title="Error",description=errors.title())
        await ctx.send(embed=embed,delete_after=10)

        
    @commands.group(invoke_without_command=True)
    async def help(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            helpembed = discord.Embed(title="**Help**",description="Use >help <command name> to get full description of a command!",color = ctx.author.color)
            helpembed.add_field(name="Moderation",value="`mute` `kick` `ban` `warn` `slowmode` `giverole` `takerole` `lockchannel` `unlockchannel` `unmute` `clean` `purge` `clw` `warnings`")
            helpembed.add_field(name="**Utility**",value="`ping` `covid` `weather` `time` `avatar` `whois`")
            helpembed.add_field(name="**Voice**",value="`moveall` `move`")
            helpembed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=helpembed)
            
    
        else:
            await ctx.send(f'{ctx.author.mention} **,Use the bot-cmd channel to run the command!**',delete_after=10)

    @help.command()
    async def ban(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed= discord.Embed(title="Ban",description="Bans the Member from the Server",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value = ">kick <member> [reason]")
            embed.add_field(name="**Permissions Required**",value="Ban Members")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def mute(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed= discord.Embed(title="Mute",description="Mutes the Member from the Server. Time and Reason are required",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value = ">mute <member> [Time] [reason]")
            embed.add_field(name="**Example**",value = f'>kick @Nishant Reason')
            embed.add_field(name="**Permissions Required**",value="Manage Messages")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def kick(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed= discord.Embed(title="Kick",description="Kicks the Member from the Server",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value = ">kick <member> [reason]")
            embed.add_field(name="**Example**",value = f'>kick @Nishant Reason')
            embed.add_field(name="**Permissions Required**",value="Kick Members")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def warn(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed= discord.Embed(title="Warn",description="Warns the Member!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value = ">warn <member> [reason]")
            embed.add_field(name="**Example**",value = f'>warn @Nishant Reason')
            embed.add_field(name="**Permissions Required**",value="Manage Messages")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def slowmode(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Slowmode",description="Enables slowmode in the channel it is run in!",color=ctx.author.color)
            embed.add_field(name = "**Syntax**",value=">slowmode <time in seconds>")
            embed.add_field(name="**Permissions Required**",value="Kick Members")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def giverole(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Give Role",description="Give a certain role to the user",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">giverole <member> [Role Name]")
            embed.add_field(name="**Example**",value = f'>giverole @Nishant Administrators')
            embed.add_field(name="**Permissions Required**",value="Manage Roles")
            embed.set_thumbnail(url=ctx.author.avatar_url)

            await ctx.send(embed=embed)
    
    @help.command()
    async def takerole(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Take Role",description="Take away a certain role from the user",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">takerole <member> [Role Name]")
            embed.add_field(name="**Example**",value = f'>takerole @Nishant Administrators')
            embed.add_field(name="**Permissions Required**",value="Manage Roles")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def lockchannel(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Lock Channel",description="Locks the channel in which command is run in!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">lockchannel <channel_mention>")
            embed.add_field(name="**Permissions Required**",value="Kick Members")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def unlockchannel(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Lock Channel",description="Unlocks the channel in which command is run in!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">unlockchannel <channel_mention>")
            embed.add_field(name="**Permissions Required**",value="Kick Members")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def unmute(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed= discord.Embed(title="Mute",description="Unmutes the Member from the Server. Reason is required!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value = ">unmute <member> [reason]")
            embed.add_field(name="**Example**",value = f'>unmute @Nishant Reason')
            embed.add_field(name="**Permissions Required**",value="Manage Messages")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def covid(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="COVID-19 Stats",description="Returns the full COVID-19 Stats of the specified country!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">covid [country_name]")
            embed.add_field(name="**Permissions Required**",value="None")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def nepse(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Nepse",description="Returns the full data of the Company specified!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">nepse [company_symbol]")
            embed.add_field(name="**Permissions Required**",value="None")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
    
    @help.command()
    async def weather(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Weather",description="Returns the Weather of the Place Specified!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">weather [place_name]")
            embed.add_field(name="**Permissions Required**",value="None")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    

    @help.command()
    async def ping(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Ping",description="Returns the Bot Latency!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">ping")
            embed.add_field(name="**Permissions Required**",value="None")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def whois(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Whois",description="See information about a member!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">whois <user_mention>")
            embed.add_field(name="**Permissions Required**",value="None")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def avatar(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Avatar",description="View the avatar of the member mentioned!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">avatar <user_mention>")
            embed.add_field(name="**Permissions Required**",value="None")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    

    
    
    @help.command()
    async def clean(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Clean",description="Deletes the Amount of messages specified. If not specified deletes 100!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">clean [number of messages]")
            embed.add_field(name="**Permissions Required**",value="Manage Messages")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def clw(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Clear Warning",description="Clears the warning of the user specified!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">clw <member mention>")
            embed.add_field(name="**Permissions Required**",value="Kick Members")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def purge(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Purge Message",description="Purge Message of the User Specified!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">purge <member mention> [number of messages]")
            embed.add_field(name="**Permissions Required**",value="Manage Messages")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def warnings(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="View Warnings",description="View Warnings of the User Specified!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">warnings <member mention> ")
            embed.add_field(name="**Permissions Required**",value="Manage Messages")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def moveall(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Move All",description="Move all the members in the Current Voice channel to the specified voice channel!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">moveall <voice channel id> ")
            embed.add_field(name="**Permissions Required**",value="Move Members")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @help.command()
    async def move(self,ctx):
        bot_commands = self.client.get_channel(835776259840802846)
        staff_bot_commands = self.client.get_channel(834643567996698644)
        amdin = self.client.get_channel(834625645936902154)

        if bot_commands == ctx.channel or staff_bot_commands == ctx.channel or amdin == ctx.channel:
            embed = discord.Embed(title="Move",description="Move the specified user to the specified voice channel!",color=ctx.author.color)
            embed.add_field(name="**Syntax**",value=">move <user mention> <voice channel id> ")
            embed.add_field(name="**Permissions Required**",value="Move Members")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))