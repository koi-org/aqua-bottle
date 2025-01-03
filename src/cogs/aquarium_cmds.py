import discord
from discord.ext import commands
from classes.manager import Manager
from classes.aquarium import Aquarium
from classes.fish import Fish


class AquariumCommands(commands.Cog):
    """
    A Cog that provides commands for managing aquariums, fish, and plants in a Discord bot.

    This class defines slash commands for creating aquariums, adding fish, and other related tasks.
    """

    def __init__(self, bot):
        """
        Initializes the AquariumCommands Cog.

        Parameters:
            bot (commands.Bot): The Discord bot instance to which this Cog is added.
        """
        self.bot = bot

    aquarium = discord.SlashCommandGroup("aquarium", "Manage your aquarium.")
    fish = aquarium.create_subgroup("fish", "Manage the fish in your aquarium.")
    plant = aquarium.create_subgroup("plant", "Manage the plants in your aquarium.")

    @discord.slash_command(
        name="create_aquarium",
        description="Create your own aquarium with your registered account!",
        guild_ids=[692964332643942463],
    )
    async def create_aquarium(self, ctx: discord.ApplicationContext, volume: int):
        """
        Slash command to create a new aquarium.

        Parameters:
            ctx (discord.ApplicationContext): The context of the command.
            volume (int): The volume of the aquarium in liters.

        Responds with a success or failure message based on whether the aquarium is created.
        """
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
            await ctx.respond("Aquarium already exists!")
        else:
            await ctx.respond(
                f"Aquarium of {volume} litres has been successfully created!"
            )

    @discord.slash_command(
        name="add_fish",
        description="Add fish to your own aquarium!",
        guild_ids=[692964332643942463],
    )
    async def add_fish(
        self, ctx: discord.ApplicationContext, species: str, gender: str, age: str
    ):
        """
        Slash command to add a fish to an existing aquarium.

        Parameters:
            ctx (discord.ApplicationContext): The context of the command.
            species (str): The species of the fish to add.
            gender (str): The gender of the fish.
            age (str): The age of the fish.

        Responds with a success or failure message based on the validity of the input and the aquarium's existence.
        """
        # check if user exists
        user_id = ctx.author.id
        channel_id = ctx.channel.id
        user = Manager.get_user(user_id)

        if user is None:
            await ctx.respond(
                "You are not a valid user, please register before creating an aquarium!"
            )
            return

        # check if the aquarium exists
        aquarium = user.get_aquarium(channel_id)
        if not aquarium:
            await ctx.respond("Aquarium does not exist!")
            return

        if species not in Aquarium.valid_fish:
            await ctx.respond(f"{species} is not a valid fish!")
        else:
            aquarium.add_fish(Fish(species, gender, int(age)))
            await ctx.respond(
                f"Fish of species: {species}, gender: {gender}, age: {age} is successfully added!"
            )


def setup(bot):
    """
    Sets up the AquariumCommands Cog in the bot.

    Parameters:
        bot (commands.Bot): The Discord bot instance.
    """
    bot.add_cog(AquariumCommands(bot))
