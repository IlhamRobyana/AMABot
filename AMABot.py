# Work with Python 3.6

import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext import commands

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello " + ctx.message.author.mention)

@bot.command()
async def roll(ctx):
    dice = random.randint(1,101)
    await ctx.send(ctx.message.author.mention + " rolled " + str(dice))

@bot.command()
async def padoru(ctx):
    await ctx.send("https://media.discordapp.net/attachments/460643534685470730/506770854252642304/spindoru_fast.gif")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

async def list_servers():
    await bot.wait_until_ready()
    while not bot.is_closed:
        print("Current servers:")
        for server in bot.servers:
            print(server.name)
        await asyncio.sleep(600)

# client.loop.create_task(list_servers())
bot.run(TOKEN)
