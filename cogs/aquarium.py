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
        user_id = str(interaction.user.id)
        ret_string = "Unexpected error occured."
        async with self.bot.db.connection() as conn:
            async with conn.cursor() as cursor:
                try:
                    query = 'insert into "Aquariums" (id, "user") values (%s, %s)'
                    await cursor.execute(query, (uuid4(), user_id))
                    await conn.commit()
                    ret_string = "Your aquarium has been successfully created!"
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
