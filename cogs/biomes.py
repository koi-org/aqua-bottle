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
            color=discord.Color.teal(),
        )
        embed.add_field(name="Fish Species", value=", ".join(fish_list), inline=False)
        await interaction.response.send_message(embed=embed)

    @biomes.command(name="fish", description="Show detailed info about a fish")
    @app_commands.describe(fish_name="Name of the fish to lookup")
    async def fish(self, interaction: discord.Interaction, fish_name: str):
        fish_info = get_fish_info(fish_name.title())
        if not fish_info:
            await interaction.response.send_message(
                f"❌ No info found for fish named '{fish_name}'."
            )
            return

        embed = discord.Embed(
            title=f"🐟 {fish_name.title()}",
            description=fish_info.get("description", "No description available."),
            color=discord.Color.gold(),
        )
        embed.add_field(
            name="Rarity", value=fish_info.get("rarity", "Unknown"), inline=True
        )
        embed.add_field(
            name="Average Size",
            value=f"{fish_info.get('size_cm', '?')} cm",
            inline=True,
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Biomes(bot))
