import discord
from discord.ext import commands
from discord import app_commands
from game.biome_manager import get_biome_for_channel, get_fish_info

class Biomes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    biomes = discord.app_commands.Group(name="biomes", description="...")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")
async def setup(bot):
    await bot.add_cog(Biomes(bot))
