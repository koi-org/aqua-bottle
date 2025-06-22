import discord
from discord.ext import commands
from uuid import uuid4
from psycopg.errors import UniqueViolation, ForeignKeyViolation


class Aquarium(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    aquarium = discord.app_commands.Group(name="bottle", description="...")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @discord.app_commands.command(name="stats", description="Get aquarium stats")
    async def stats(self, interaction: discord.Interaction):
        await interaction.response.send_message("Reveal stats!")

    @aquarium.command(name="create", description="Create aquarium!")
    async def create(self, interaction: discord.Interaction):
        # Check if the interaction is in a valid server text channel
        if interaction.channel is None or not isinstance(interaction.channel, discord.TextChannel):
            await interaction.response.send_message(
                "This command must be used in a server text channel.",
                ephemeral=True
            )
            return

        user_id = str(interaction.user.id)
        channel_id = interaction.channel.id
        ret_string = "Unexpected error occurred."

        async with self.bot.db.connection() as conn:
            async with conn.cursor() as cursor:
                try:
                    query = 'INSERT INTO "Aquariums" (id, "user", channel_id) VALUES (%s, %s, %s)'
                    await cursor.execute(query, (uuid4(), user_id, channel_id))
                    await conn.commit()
                    ret_string = f"Aquarium created and loaded in <#{channel_id}>!"
                except UniqueViolation:
                    ret_string = "User already has an aquarium"
                except ForeignKeyViolation:
                    ret_string = "User not found"
                except Exception as e:
                    print("error", e)

        await interaction.response.send_message(ret_string)

    @discord.app_commands.command(name="feed", description="Feed fish")
    async def feed(self, interaction: discord.Interaction):
        await interaction.response.send_message("Fed fish")


async def setup(bot):
    await bot.add_cog(Aquarium(bot, bot.db))
