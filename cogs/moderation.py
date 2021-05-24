import discord 
from discord.ext import commands
import asyncio

class Moderation(commands.Cog):

    def __init__(self,client):
        self.client = client
    

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member:discord.Member,*,reason=None):
        if member.top_role >= ctx.author.top_role:
            await ctx.send("**You cannot run moderation commands on the users on same rank or higher than you!**")
            await ctx.message.delete()
        else:
            await member.kick(reason=reason)
            embed = discord.Embed(title="Kick",description=f'{member.mention} has been kicked!',color=0xff0000)
            embed.add_field(name="**Reason**",value=reason,inline=True)
            embed.add_field(name="**Kicked By**",value=ctx.author,inline=True)
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed)
            #Send in Mod-Logs
            mod_logs = self.client.get_channel(834624217466667048)
            await mod_logs.send(embed = embed)
            await ctx.message.delete()
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member:discord.Member,*,reason=None):
        if member.top_role >= ctx.author.top_role:
            await ctx.send("**You cannot run moderation commands on the users on same rank or higher than you!**")
            await ctx.message.delete()
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(title="Ban",description=f'{member.mention} has been banned!',color=0xff0000)
            embed.add_field(name="**Reason**",value=reason,inline=True)
            embed.add_field(name="**Banned By**",value=ctx.author,inline=True)
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed)
            #Send in Mod-Logs
            mod_logs = self.client.get_channel(834624217466667048)
            await mod_logs.send(embed = embed)
            await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def slowmode(self,ctx,seconds:int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!",delete_after=5)
        await ctx.message.delete()
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def lockchannel(self,ctx,channel : discord.TextChannel=None):
        channel = ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role,overwrite=overwrite)
        await ctx.send(f"<#{channel.id}> has been locked!")
        await ctx.message.delete()
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unlockchannel(self,ctx,channel:discord.TextChannel=None):
        channel = ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role,overwrite=overwrite)
        await ctx.send(f"<#{channel.id}> has been unlocked!")
        await ctx.message.delete()
    
    

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def giverole(self,ctx,member:discord.Member,args):
        if member.top_role >= ctx.author.top_role:
            await ctx.send("**You cannot run giverole commands on the users on same rank or higher than you!**")
            await ctx.message.delete()
        
        else:
            role = discord.utils.get(ctx.guild.roles,name=args)
            await member.add_roles(role)
            await ctx.send(f'Gave {role} to {member}!',delete_after=5)
            await ctx.message.delete()
    

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def takerole(self,ctx,member:discord.Member,args):
        if member.top_role >= ctx.author.top_role:
            await ctx.send("**You cannot run takerole commands on the users on same rank or higher than you!**")
            await ctx.message.delete()
        else:
            role = discord.utils.get(ctx.guild.roles,name=args)
            await member.remove_roles(role)
            await ctx.send(f'Removed {role} from {member}!',delete_after=5)
            await ctx.message.delete()
    
    #SEND MESSAGE TO SPECIFIC CHANNEL USING BOT
    @commands.command()
    @commands.has_role('Custom Commands')
    async def send(self,ctx,channel:discord.TextChannel,args):
        await channel.send(args)
        await ctx.message.delete()
    

    @commands.command()
    @commands.has_any_role("Administrators","Moderators")
    async def clean(self,ctx,number=100):
        await ctx.channel.purge(limit=int(number)+1)
        await ctx.send("Messages deleted!",delete_after=3)

    @commands.command()
    @commands.has_any_role("Administrators","Moderators")
    async def purge(self,ctx,member:discord.Member,number=100):
        await ctx.channel.purge(limit=int(number)+1,check=lambda x: x.author == member)

        

def setup(client):
    client.add_cog(Moderation(client))
