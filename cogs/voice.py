import discord

from discord.ext import commands
from discord.ext.commands import check
from discord import FFmpegPCMAudio
from discord.utils import get
import os

class Voice(commands.Cog):
    
    def __init__(self,client):
        self.client = client
    
    def in_voice_channel():
        def predicate(ctx):
            return ctx.author.voice and ctx.author.voice.channel
        return check(predicate)

    @in_voice_channel()
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def moveall(self,ctx,*,channel:discord.VoiceChannel):
        for members in ctx.author.voice.channel.members:
            await members.move_to(channel)
        
        await ctx.message.delete()
    

    @in_voice_channel()
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def move(self,ctx,member:discord.Member,channel:discord.VoiceChannel):
        await member.move_to(channel)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Voice(client))
