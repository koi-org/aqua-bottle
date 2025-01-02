import discord
from discord.ext import commands
from classes.manager import Manager


class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="register",
        description="Register your account for the aquarium game!",
        guild_ids=[692964332643942463],
    )
    async def register(self, ctx: discord.ApplicationContext, username: str = None):
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
    bot.add_cog(UserCommands(bot))
