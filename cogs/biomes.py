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

    @app_commands.command(name="biome", description="Show current channel's biome info")
    async def biome(self, interaction: discord.Interaction):
        biome = get_biome_for_channel(interaction.channel_id)
        fish_list = biome["fish"]
        embed = discord.Embed(
            title=f"🌍 Biome: {biome['name']}",
            description="This channel’s fishing biome and available fish:",
            color=discord.Color.teal()
        )
        embed.add_field(name="Fish Species", value=", ".join(fish_list), inline=False)
        await interaction.response.send_message(embed=embed)
async def setup(bot):
    await bot.add_cog(Biomes(bot))
