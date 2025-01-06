import discord
from discord.ext import commands
from classes.manager import Manager
from classes.aquarium import Aquarium
from classes.fish import Fish
from classes.plant import Plant


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

    @aquarium.command(
        name="create",
        description="Create your own aquarium with your registered account!",
        guild_ids=[692964332643942463],
    )
    async def create(
        self,
        ctx: discord.ApplicationContext,
        substrate: str = discord.Option(str, choices=Aquarium.VALID_SUBSTRATE),
        volume: int = 50,
    ):
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
        aquarium = Aquarium(channel_id, volume, substrate)
        append_aquarium = user.add_aquarium(aquarium)

        if not append_aquarium:
            await ctx.respond("Aquarium already exists!")
        else:
            await ctx.respond(
                f"Aquarium of {volume} litres with substrate {substrate} has been successfully created!"
            )

    @aquarium.command(
        name="remove",
        description="Remove this channel's aquarium.",
        guild_ids=[692964332643942463],
    )
    async def remove(self, ctx: discord.ApplicationContext):
        user_id = ctx.author.id
        channel_id = ctx.channel.id
        user = Manager.get_user(user_id)

        # Check if user is valid
        if user is None:
            await ctx.respond(
                "You are not a valid user, please register before creating an aquarium!"
            )
            return

        aquarium = user.get_aquarium(channel_id)
        if aquarium is None:
            await ctx.respond("Aquarium does not exist")
        else:
            await ctx.respond(
                f"Aquarium of age: {aquarium.age} time units is getting removed..."
            )
            aquarium.stop()
            user.remove_aquarium(aquarium)
            await ctx.respond("Aquarium successfully removed!")

    @aquarium.command(
        name="feed",
        description="Feed fish",
        guild_ids=[692964332643942463],
    )
    async def feed_fish(self, ctx: discord.ApplicationContext):
        user_id = ctx.author.id
        channel_id = ctx.channel.id
        user = Manager.get_user(user_id)

        # Check if user is valid
        if user is None:
            await ctx.respond(
                "You are not a valid user, please register before creating an aquarium!"
            )
            return

        aquarium = user.get_aquarium(channel_id)
        if aquarium is None:
            await ctx.respond("Aquarium does not exist")
            return

        if aquarium.inhabitants["fish"] == set():
            await ctx.respond("No fish in aquarium, starting nitrogen cycle")
        else:
            await ctx.respond("Fed fish")

        aquarium.feed()

    @aquarium.command(
        name="water_change",
        description="do a water change",
        guild_ids=[692964332643942463],
    )
    async def water_change(self, ctx: discord.ApplicationContext, volume: int):
        user_id = ctx.author.id
        channel_id = ctx.channel.id
        user = Manager.get_user(user_id)

        # Check if user is valid
        if user is None:
            await ctx.respond(
                "You are not a valid user, please register before creating an aquarium!"
            )
            return

        aquarium = user.get_aquarium(channel_id)
        if aquarium is None:
            await ctx.respond("Aquarium does not exist")
            return

        if not aquarium.water_change(volume):
            await ctx.respond(
                f"""Volume higher than your tank! Please input a number less than {aquarium.volume}!"""
            )
        else:
            await ctx.respond(
                f"""Completed water change! your new water quality is {aquarium.water_quality}"""
            )

    @fish.command(
        name="add",
        description="Add fish to your own aquarium!",
        guild_ids=[692964332643942463],
    )
    async def add_fish(
        self,
        ctx: discord.ApplicationContext,
        species: str = discord.Option(str, choices=Fish.VALID_FISH),
        gender: str = discord.Option(choices=["Male", "Female"]),
        age: int = 0,
    ):
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

        aquarium.add_fish(Fish(species, gender, int(age)))
        await ctx.respond(
            f"Fish of species: {species}, gender: {gender}, age: {age} is successfully added!"
        )

    @plant.command(
        name="add",
        description="Add plants to your aquarium!",
        guild_ids=[692964332643942463],
    )
    async def add_plant(
        self,
        ctx: discord.ApplicationContext,
        species: str = discord.Option(str, choices=Plant.VALID_PLANTS),
    ):
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

        aquarium.add_plant(Plant(species))
        await ctx.respond(f"Plant of species: {species} is successfully added!")


def setup(bot):
    """
    Sets up the AquariumCommands Cog in the bot.

    Parameters:
        bot (commands.Bot): The Discord bot instance.
    """
    bot.add_cog(AquariumCommands(bot))
