import discord
from discord.ext import commands

class Aquarium(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @discord.app_commands.command(name="stats", description="Get aquarium stats")
    async def stats(self, interaction: discord.Interaction):
        await interaction.response.send_message("Reveal stats!")

    @discord.app_commands.command(name="create", description="Create aquarium!")
    async def create(self, interaction: discord.Interaction):
        await interaction.response.send_message("Created aquarium!")

    @discord.app_commands.command(name="feed", description="Feed fish")
    async def feed(self, interaction: discord.Interaction):
        await interaction.response.send_message("Fed fish")


async def setup(bot):
    await bot.add_cog(Aquarium(bot))