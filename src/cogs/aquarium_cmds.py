import discord
from discord.ext import commands
from classes.manager import Manager
from classes.aquarium import Aquarium
from classes.fish import Fish


class AquariumCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="create_aquarium",
        description="Create your own aquarium with your registered account!",
        guild_ids=[692964332643942463],
    )
    async def create_aquarium(self, ctx: discord.ApplicationContext, volume: int):
        user_id = ctx.author.id
        channel_id = ctx.channel.id
        user = Manager.get_user(user_id)

        # Check if user is valid
        if user is None:
            await ctx.respond(
                "You are not a valid user, please register before creating an aquarium!"
            )
            return

        # check if the aquarium already exists
        aquarium = Aquarium(channel_id, volume)
        append_aquarium = user.add_aquarium(aquarium)

        if not append_aquarium:
            await ctx.respond(f"Aquarium already exists!")
        else:
            await ctx.respond(f"Aquarium has been successfully created!")

    @discord.slash_command(
        name="add_fish",
        description="Add fish to your own aquarium!",
        guild_ids=[692964332643942463],
    )
    async def add_fish(
        self, ctx: discord.ApplicationContext, species: str, gender: str, age: str
    ):
        # check if user exists
        user_id = ctx.author.id
        channel_id = ctx.channel.id
        user = Manager.get_user(user_id)

        # check if aquarium exists
        if user is None:
            await ctx.respond(
                "You are not a valid user, please register before creating an aquarium!"
            )

        aquarium = user.get_aquarium(channel_id)
        # check if the aquarium exists
        if not aquarium:
            await ctx.respond("Aquarium does not exist!")

        new_fish = Fish(species, gender, int(age))
        # check if the fish is a valid species
        valid_fish = aquarium.is_valid_fish(new_fish)

        if not valid_fish:
            await ctx.respond("Fish is not valid!")

        else:
            aquarium.add_fish(new_fish)
            await ctx.respond(f"Fish successfully added!")

        channel_id = ctx.channel.id


def setup(bot):
    bot.add_cog(AquariumCommands(bot))
