import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self,client):
        self.client = client



    @commands.Cog.listener()
    async def on_message(self,message):
        if message.channel.id == 834478616158928918:
                if message.attachments:
                    emoji_1 = "<:IT_cursedkek:834834181123997726>"
                    emoji_2 = "<:IT_bonk:839138589655826452>"
                    await message.add_reaction(emoji_1)
                    await message.add_reaction(emoji_2)
                
                if message.channel.id == 834478616158928918:
                    media_ext = ['.jpg','.png','.jpeg','.mp4','.gif']
                    for ext in media_ext:
                        if message.content.endswith(ext):
                            emoji_1 = "<:IT_cursedkek:834834181123997726>"
                            emoji_2 = "<:IT_bonk:839138589655826452>"
                            await message.add_reaction(emoji_1)
                            await message.add_reaction(emoji_2)

        member = await self.client.fetch_user(479886922471440385)
        if member.mentioned_in(message):
            if message.reference:
                pass
            else:
                emoji = "<:IT_bonk:839138589655826452>"
                emoji2 = "<:IT_gun:834833978053230623>"
                emoji3 = "<:IT_flyingchappal:836965053969203220>"
                await message.add_reaction(emoji)
                await message.add_reaction(emoji2)
                await message.add_reaction(emoji3)
        
        amdin = await self.client.fetch_user(775542341363957780)
        if amdin.mentioned_in(message):
            if message.reference:
                pass
            else:
                emoji = "<:IT_bonk:839138589655826452>"
                emoji2 = "<:IT_gun:834833978053230623>"
                emoji3 = "<:IT_flyingchappal:836965053969203220>"
                await message.add_reaction(emoji)
                await message.add_reaction(emoji2)
                await message.add_reaction(emoji3)
            

def setup(client):
    client.add_cog(Events(client))