import discord
from discord.ext import commands
import datetime
from dotenv import load_dotenv
from pathlib import Path
import os
import requests
import aiohttp

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


class Fun(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def avatar(self,ctx,member:discord.Member=None):

        if not member:
            member = ctx.message.author

        userAvatarUrl = member.avatar_url
        embed = discord.Embed(title="Avatar Showcase",color=ctx.author.color)
        embed.set_image(url=userAvatarUrl)
            
        await ctx.send(embed=embed)
    
    @commands.command()
    async def whois(self,ctx,member:discord.Member=None):
        if not member:
            member = ctx.message.author
        embed = discord.Embed(title=f'User Info - {member}',timestamp = ctx.message.created_at,color = ctx.author.color)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}')
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)

        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Highest Role:", value=member.top_role.mention)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def doggo(self,ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dog_json = await request.json()

        embed = discord.Embed(title="Here's a doggo for you!",color=ctx.author.color)
        embed.set_image(url=dog_json["link"])
        embed.set_footer(text=f"Requested by {ctx.author.name}")

        await ctx.send(embed=embed)
    
    @commands.command()
    async def cat(self,ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            cat_json = await request.json()
        embed = discord.Embed(title="Here's a cat for you!", color=ctx.author.color) 
        embed.set_image(url=cat_json['link'])
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_message(self,message):
        if 'lmao' in message.content:
            emoji = "<:pikakek:834840515814883360>"
            await message.add_reaction(emoji)
        
        if 'leanbow' in message.content:
            emoji = "<:pikakek:834840515814883360>"
            await message.add_reaction(emoji)

    @commands.command()
    async def panda(self,ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/panda')
            panda_json = await request.json()
        embed = discord.Embed(title="Here's a panda for you!",color=ctx.author.color)
        embed.set_image(url=panda_json['link'])
        embed.set_footer(text=f"Requested by {ctx.author.name}")

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Fun(client))
