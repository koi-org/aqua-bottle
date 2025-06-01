import asyncio
import os
from dotenv import load_dotenv, find_dotenv
import discord
from discord.ext import commands
from psycopg_pool import AsyncConnectionPool
from bot import Bot

env_path = find_dotenv(usecwd=True)
load_dotenv(dotenv_path=env_path, verbose=True, override=True)


intents = discord.Intents.default()
intents.message_content = True


TOKEN = os.getenv("DISCORD_TOKEN")
SERVER_ID = os.getenv("DEFAULT_GUILD")
DATABASE_URI = os.getenv("DATABASE_URI")


async def run():
    if not DATABASE_URI:
        print("Error: DATABASE_URI not found. Make sure it's set in your .env file.")
        return
    if not TOKEN:
        print("Error: DISCORD_TOKEN not found. Make sure it's set in your .env file.")
        return

    pool = AsyncConnectionPool(DATABASE_URI, open=False)
    await pool.open()

    bot = Bot(prefix="!", intents=intents, db=pool)

    @bot.command(name="sync")
    async def sync_commands(ctx: commands.Context):
        await ctx.send("Syncing global commands...")
        try:
            synced = await bot.tree.sync()
            await ctx.send(f"Synced {len(synced)} commands globally.")
        except Exception as e:
            await ctx.send(f"Error syncing commands: {e}")

    try:
        await bot.start(TOKEN)
    except KeyboardInterrupt:
        print("Bot shutting down...")
    finally:
        if "pool" in locals() and pool:
            await pool.close()
            print("Database pool closed.")
        if "bot" in locals() and bot:
            await bot.close()
            print("Bot logged out.")


if __name__ == "__main__":
    asyncio.run(run())
