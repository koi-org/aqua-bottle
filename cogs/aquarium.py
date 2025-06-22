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

    async def is_aquarium_loaded(self, user_id: str, channel_id: int):
        async with self.bot.db.connection() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute('SELECT channel_id FROM "Aquariums" WHERE "user" = %s', (user_id,))
                result = await cursor.fetchone()
                return result and result[0] == channel_id

    @aquarium.command(name="stats", description="Get aquarium stats")
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

    @aquarium.command(name="load", description="Load your aquarium to this channel")
    async def load(self, interaction: discord.Interaction):
        if interaction.channel is None or not isinstance(interaction.channel, discord.TextChannel):
            await interaction.response.send_message(
                "This command must be used in a server text channel.",
                ephemeral=True
            )
            return

        channel_id = interaction.channel.id

        user_id = str(interaction.user.id)
        async with self.bot.db.connection() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute('SELECT id FROM "Aquariums" WHERE "user" = %s', (user_id,))
                exists = await cursor.fetchone()
                if not exists:
                    await interaction.response.send_message("You don't have an aquarium to load.", ephemeral=True)
                    return

                await cursor.execute('UPDATE "Aquariums" SET channel_id = %s WHERE "user" = %s',
                                     (channel_id, user_id))
                await conn.commit()
                await interaction.response.send_message(f"Aquarium loaded into <#{channel_id}>!")


    @discord.app_commands.command(name="feed", description="Feed fish")
    async def feed(self, interaction: discord.Interaction):
        await interaction.response.send_message("Fed fish")


async def setup(bot):
    await bot.add_cog(Aquarium(bot, bot.db))
