import discord
from discord.ext import commands

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @discord.app_commands.command(name="ping", description="Replies with Pong!")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")

    @discord.app_commands.command(name='register', description="Registers user!")
    async def register(self, interaction: discord.Interaction):
        await interaction.response.send_message("Registered!")

async def setup(bot):
    await bot.add_cog(User(bot))