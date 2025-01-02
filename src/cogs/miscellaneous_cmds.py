import discord
from discord.ext import commands


class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="hello", description="Say hello to the bot", guild_ids=[692964332643942463]
    )
    async def hello(self, ctx: discord.ApplicationContext):
        username = ctx.author.name
        user_id = ctx.author.id
        channel_id = ctx.channel.id
        channel_name = ctx.channel.name
        guild_id = ctx.guild.id

        await ctx.respond(
            f"Hello {username} (User ID: {user_id})! You are in channel {channel_name} (ID: {channel_id}). (Guild id: {guild_id})"
        )


def setup(bot):
    bot.add_cog(Miscellaneous(bot))
