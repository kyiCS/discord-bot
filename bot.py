# bot.py

# What do i want this bot to-do?
# - TLK word registry
# - summoners war search?
# - league of legends build

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild)
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
