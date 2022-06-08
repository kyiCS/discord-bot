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

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        if message.content == '/shutdown':
            await self.logout()


client = MyClient()
client.run(TOKEN)
