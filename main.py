import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='>',intents=intents)
client.remove_command('help')

@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
