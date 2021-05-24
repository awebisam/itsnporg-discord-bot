import discord
from discord.ext import commands
import json
import os


with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []


class Warn(commands.Cog):

    def __init__(self,client):
        self.client = client

    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self,ctx,member:discord.Member,*reason:str):

        if member.top_role >= ctx.author.top_role:
            await ctx.send("**You cannot run moderation commands on the users on same rank or higher than you!**")
            await ctx.message.delete()
        
        else:
            if not reason:
                await ctx.send("Please provide a reason")
                return
            reason = ' '.join(reason)

            embed = discord.Embed(title="Warning",description=f'{member} has been warned!',color=0xff0000)
            embed.add_field(name="**Reason**",value=reason,inline=True)
            embed.add_field(name="**Warned By**",value=ctx.author,inline=True)
            await ctx.send(embed=embed)
            mod_logs = self.client.get_channel(834624217466667048)
            await mod_logs.send(embed = embed)
            await member.send(f'You have been warned for {reason}!')

            try:
                for current_user in report['users']:
                    if current_user['name'] == member.name:
                        current_user['reasons'].append(reason)
                        break
                else:
                    report['users'].append({
                    'name':member.name,
                    'reasons': [reason,]
                    })
                with open('reports.json','w+') as f:
                    json.dump(report,f)

                with open('reports.json','w+') as f:
                    json.dump(report,f)
            
                if len(report['users']) >= 7:
                    await member.kick(reason='You reached 7 warnings')
            
            except:
                newlist = filter(lambda x : len(x)>0 , report["users"])
                for current_user in newlist:
                    if current_user['name'] == member.name:
                        current_user['reasons'].append(reason)
                        break
                else:
                    report['users'].append({
                    'name':member.name,
                    'reasons': [reason,]
                    })
                with open('reports.json','w+') as f:
                    json.dump(report,f)

                with open('reports.json','w+') as f:
                    json.dump(report,f)
            
                if len(report['users']) >= 7:
                    await member.kick(reason='You reached 7 warnings')
    

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warnings(self,ctx,user:discord.User):
        try:
            for current_user in report['users']:
                if user.name == current_user['name']:
                        await ctx.send(f"**{user.name} has been warned {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}**")
                        break
            else:
                await ctx.send(f"**{user.name} has never been reported**")
        except:
            newlist = filter(lambda x : len(x)>0 , report["users"])
            for current_user in newlist:
                if user.name == current_user['name']:
                    try:
                        await ctx.send(f"**{user.name} has been warned {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}**")
                        break
                    except:
                        await ctx.send(f'**{user.name} has never been warned!**')
            else:
                await ctx.send(f"**{user.name} has never been reported**")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def clw(self,ctx,user:discord.User):
        try:
            for current_user in report['users']:
                if user.name == current_user['name']:
                    current_user.pop('reasons')
                    current_user.pop('name')
                    with open('reports.json','w+') as f:
                        json.dump(report,f)
                    await ctx.send(f'Warnings of {user} cleared sucessfully!')
        except:
            newlist = filter(lambda x : len(x)>0 , report["users"])
            for current_user in newlist:
                if user.name == current_user['name']:
                    current_user.pop('reasons')
                    current_user.pop('name')
                    with open('reports.json','w+') as f:
                        json.dump(report,f)
                    await ctx.send(f'Warnings of {user} cleared sucessfully!')


def setup(client):
    client.add_cog(Warn(client))