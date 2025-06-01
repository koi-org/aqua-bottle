import os
import sys
import traceback

import discord
from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self, prefix, intents, db, **kwargs):
        super().__init__(command_prefix=prefix, intents=intents, **kwargs)
        self.db = db

    async def setup_hook(self):
        print("Running setup_hook...")
        cogs_dir = "./cogs"
        if not os.path.isdir(cogs_dir):
            print(
                f"Warning: Cogs directory '{cogs_dir}' not found. No cogs will be loaded."
            )
            return

        for filename in os.listdir(cogs_dir):
            if filename.endswith(".py") and not filename.startswith("_"):
                try:
                    await self.load_extension(f"cogs.{filename[:-3]}")
                    print(f"Successfully loaded cog: cogs.{filename[:-3]}")
                except commands.ExtensionError as e:
                    print(
                        f"Failed to load cog cogs.{filename[:-3]}: {e.__class__.__name__} - {e}",
                        file=sys.stderr,
                    )
                    traceback.print_exc()

    async def on_ready(self):
        print(f"Bot ready. Logged in as {self.user} (ID: {self.user.id})")
        print("------")
