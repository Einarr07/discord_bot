import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")


async def load_extension():
    extensions = ["cogs.roles", "cogs.welcome", "cogs.reminders"]
    for extension in extensions:
        await bot.load_extension(extension)


async def main():
    async with bot:
        await load_extension()
        await bot.start(TOKEN)


asyncio.run(main())
