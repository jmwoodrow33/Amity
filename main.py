from itertools import cycle
import discord
from discord.ext import commands
import logging
import os
import config

logging.basicConfig(level=logging.INFO)  # Log INFO level messages and above
logger = logging.getLogger(__name__)

TOKEN = config.TOKEN

client = commands.Bot(command_prefix='!!', intents=discord.Intents.all())

botStatus = cycle(["Listening :)"])

@client.event
async def on_ready():
    print("Bot is connected to discord")
    
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cog_name = f"cogs.{filename[:-3]}"
            try:
                await client.load_extension(cog_name)  # Use await here
                logger.info(f"Successfully loaded cog: {cog_name}")
            except Exception as e:
                logger.error(f"Failed to load cog: {cog_name}", exc_info=True)
    
client.run(TOKEN)