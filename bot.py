import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio
from psycopg_pool import AsyncConnectionPool

intents = discord.Intents.default()
intents.message_content = True


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER_ID = os.getenv("DEFAULT_GUILD")
DATABASE_URI = os.getenv("DATABASE_URI")

pool = AsyncConnectionPool(DATABASE_URI, open=False)

bot = commands.Bot(command_prefix="!", intents=intents, db=pool)


@bot.hybrid_command()
async def sync(ctx: commands.Context):
    await ctx.send("Syncing... ")
    await bot.tree.sync()


@bot.event
async def on_ready():
    print("Bot ready")


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)


asyncio.run(main())
