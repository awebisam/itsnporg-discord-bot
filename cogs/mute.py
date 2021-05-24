import discord
from discord.ext import commands
import json
import asyncio




with open('muted_history.json', encoding='utf-8') as f:
  try:
    muted = json.load(f)
  except ValueError:
    muted = {}
    muted['users'] = []

class Mute(commands.Cog):

    def __init__(self,client):
        self.client = client
    


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self,ctx,member:discord.Member,time,reason):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles,name="Muted")
        number_filter = filter(str.isdigit,time)
        string_filter = filter(str.isalpha,time)
        number = "".join(number_filter)
        string = "".join(string_filter)

        if member.top_role >= ctx.author.top_role:
            await ctx.send("**You cannot run moderation commands on the users on same rank or higher than you!**")
            await ctx.message.delete()
        
        else:
            await member.add_roles(mutedRole)
            embed = discord.Embed(title="Mute",description=f'{member.mention} has been muted for {time}!' ,color=0xff0000)
            embed.add_field(name="**Reason**",value=reason,inline=True)
            embed.add_field(name="**Muted By**",value=ctx.author,inline=True)
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed)
            #Send in Mod-Logs
            mod_logs = self.client.get_channel(834624217466667048)
            await mod_logs.send(embed = embed)
            await member.send(f'You have been muted from {guild} for {time}!')
            await ctx.message.delete()

            try:
                for current_user in muted['users']:
                    if current_user['name'] == member.name:
                        current_user['reasons'].append(reason)
                        break
                else:
                    muted['users'].append({
                    'name':member.name,
                    'reasons': [reason,]
                    })
                with open('muted_history.json','w+') as f:
                    json.dump(muted,f)

                with open('muted_history.json','w+') as f:
                    json.dump(muted,f)

            except:
                newlist = filter(lambda x : len(x)>0 , muted["users"])
                for current_user in newlist:
                    if current_user['name'] == member.name:
                        current_user['reasons'].append(reason)
                        break
                else:
                    muted['users'].append({
                    'name':member.name,
                    'reasons': [reason,]
                    })
                with open('muted_history.json','w+') as f:
                    json.dump(muted,f)

                with open('muted_history.json','w+') as f:
                    json.dump(muted,f)

            if str(string) == "s":
                await asyncio.sleep(int(number))
                            
            if str(string) == "m":
                await asyncio.sleep(int(number)*60)
                            
            if str(string) == "h":
                await asyncio.sleep(int(number)*3600)
                            
            if str(string) == "d":
                await asyncio.sleep(int(number)*86400)
                    
            if mutedRole in member.roles:
                await member.remove_roles(mutedRole)
                embed = discord.Embed(title="Mute",description=f'{member.mention} has been unmuted!',color=0x00ff00)
                embed.add_field(name="**Reason**",value="Mute Duration Expired!",inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                await ctx.send(embed = embed)
                #Send in Mod-Logs
                mod_logs = self.client.get_channel(834624217466667048)
                await mod_logs.send(embed = embed)
                await ctx.send(embed = embed)
                await member.send(f'You have been unmuted from {guild}!')
                try:
                    for current_user in muted['users']:
                        if member.name == current_user['name']:
                            current_user.pop('reasons')
                            current_user.pop('name')
                            with open('muted_history.json','w+') as f:
                                json.dump(muted,f)
                except:
                    newlist = filter(lambda x : len(x)>0 , muted["users"])
                    for current_user in newlist:
                        if member.name == current_user['name']:
                            current_user.pop('reasons')
                            current_user.pop('name')
                            with open('muted_history.json','w+') as f:
                                json.dump(muted,f)
            else:
                pass
            
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self,ctx,member:discord.Member,reason):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles,name="Muted")
        if member.top_role >= ctx.author.top_role:
            await ctx.send("**You cannot run moderation commands on the users on same rank or higher than you!**")
            await ctx.message.delete()
        
        else:

            if reason == None:
                await ctx.send("Please provide a reason!",delete_after=5)
            
            else:
                if mutedRole in member.roles:
                    await member.remove_roles(mutedRole)
                    embed = discord.Embed(title="Unmute",description=f'{member.mention} has been unmuted!' ,color=0x00ff00)
                    embed.add_field(name="**Reason**",value=reason,inline=True)
                    embed.add_field(name="**Unmuted By**",value=ctx.author,inline=True)
                    embed.set_thumbnail(url=member.avatar_url)
                    await ctx.send(embed=embed)
                    #Send in Mod-Logs
                    mod_logs = self.client.get_channel(834624217466667048)
                    await mod_logs.send(embed = embed)
                    await ctx.message.delete()
                    await member.send(f'You have been unmuted from {guild}!')
                
                    try:
                        for current_user in muted['users']:
                            if member.name == current_user['name']:
                                current_user.pop('reasons')
                                current_user.pop('name')
                                with open('muted_history.json','w+') as f:
                                    json.dump(muted,f)
                    except:
                        newlist = filter(lambda x : len(x)>0 , muted["users"])
                        for current_user in newlist:
                            if member.name == current_user['name']:
                                current_user.pop('reasons')
                                current_user.pop('name')
                                with open('muted_history.json','w+') as f:
                                    json.dump(muted,f)
                else:
                    await ctx.send("User is not muted!",delete_after=5)


def setup(client):
    client.add_cog(Mute(client))
