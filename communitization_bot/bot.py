# This example requires the 'message_content' intent.

import discord
import os
from discord.ext import commands
from . import ai
import sys

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def test(ctx):
    await ctx.send("test")

@bot.command()
async def communitization(ctx, text:str):
    try:
        text = ai.ai_processing(text)
        await ctx.send(text)
    except:
        restart_bot()

def restart_bot():
  os.execv(sys.executable, ['python'] + sys.argv)

def run_bot():
    bot.run(os.getenv('DISCORD_BOT_TOKEN'))
