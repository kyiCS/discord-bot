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

    async def shutdown(ctx):
        await ctx.bot.logout()

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()
client.run(TOKEN)
