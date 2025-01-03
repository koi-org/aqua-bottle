import discord
from discord.ext import commands


class Miscellaneous(commands.Cog):
    """
    A cog command for miscellaneous commands
    """

    def __init__(self, bot):
        """
        Initialises the Miscellaneous Cog.

        Parameters:
            bot (commands.Bot): The Discord bot instance to which this Cog is added.
        """
        self.bot = bot

    @discord.slash_command(
        name="hello", description="Say hello to the bot", guild_ids=[692964332643942463]
    )
    async def hello(self, ctx: discord.ApplicationContext):
        """
        Slash command to say hello to the user

        Parameters:
            ctx (discord.ApplicationContext): The context of the command.

        Responds by saying hello to the user with their username and user id and
        channel id
        """
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
