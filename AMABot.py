# Work with Python 3.6

import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("AMA.")
TOKEN = 'NTE0NjM1NjQ5NDg4MjU3MDI1.DtZfHg.FMchMpxkqczKwm9o3tSX-T38PqU'

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='hello',pass_context=True)
async def hello(context):
    await client.say("Hello " + context.message.author.mention)

@client.command(name='roll',pass_context=True)
async def roll(context):
    dice = random.randint(1,101)
    await client.say(context.message.author.mention + " rolled " + str(dice))

@client.command()
async def padoru():
    await client.say("https://media.discordapp.net/attachments/460643534685470730/506770854252642304/spindoru_fast.gif")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=Game(name="with you"))

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

# client.loop.create_task(list_servers())
client.run(TOKEN)