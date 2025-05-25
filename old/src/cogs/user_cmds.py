import discord
from discord.ext import commands
from classes.manager import Manager


class UserCommands(commands.Cog):
    """
    A cog that provides commands for user commands
    """

    def __init__(self, bot):
        """
        Initialises the UserCommands Cog.

        Parameters:
            bot (commands. Bot): THe Discord bot instance to which this Cog is added.
        """
        self.bot = bot

    user = discord.SlashCommandGroup("user", "Manage your user account.")

    @user.command(
        name="register",
        description="Register your account for the aquarium game!",
        guild_ids=[692964332643942463],
    )
    async def register(self, ctx: discord.ApplicationContext, username: str = None):
        """
        Slash command to register a new user.

        Parameters:
            ctx (discord.ApplicationContext): The context of the command.
            volume (int): The volume of the aquarium in liters.

        Responds with a success or failure message based on whether the user has
        been successfully registered.
        """
        discord_name = ctx.author.name
        user_id = ctx.author.id

        if not username:
            username = discord_name

        if Manager.add_user(user_id, username):
            await ctx.respond(
                f"{discord_name} has successfully registered for the game as: {username}."
            )
        else:
            await ctx.respond("You're already in the game.")


def setup(bot):
    """
    Sets up the UserCommands Cog in the bot.

    Parameters:
        bot (commands.Bot): The Discord bot instance.
    """
    bot.add_cog(UserCommands(bot))
