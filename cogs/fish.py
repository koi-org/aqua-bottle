from random import choice
from uuid import uuid4
import discord
from discord.ext import commands
from  game.biome_manager import get_biome_for_channel

class Fish(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    fish = discord.app_commands.Group(name="fish", description="...")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @fish.command(name="create", description="Create fish!")
    async def create(self, interaction: discord.Interaction):
        """Create fish"""
        user_id = str(interaction.user.id)
        ret_string = "Unexpected error occured."
        async with self.bot.db.connection() as conn:
            async with conn.cursor() as cursor:
                try:
                    # check if the aquarium exists first
                    query = """select id from "Aquariums" where "user"=%s"""
                    await cursor.execute(query, (user_id,))
                    aquarium = await cursor.fetchone()

                    # if aquarium doesn't exist, print out the message
                    if not aquarium:
                        await interaction.response.send_message(
                            "Aquarium does not exist"
                        )
                        return

                    biome = get_biome_for_channel(interaction.channel_id)
                    fish_breed = choice(biome['fish'])
                    aquarium_id = aquarium[0]
                    query = """
                        insert into "Fishes" (
                            id,
                            aquarium,
                            breed,
                            age,
                            gender
                        ) values (
                            %s, %s, %s, %s, %s
                        )"""
                    await cursor.execute(
                        query,
                        (
                            str(uuid4()),
                            aquarium_id,
                            fish_breed,
                            0,
                            choice(["male", "female"]),
                        ),
                    )
                    await conn.commit()
                    ret_string = f"Fish of {fish_breed} has been created!"
                except Exception as e:
                    print("error", e)
        await interaction.response.send_message(ret_string)


async def setup(bot):
    await bot.add_cog(Fish(bot, bot.db))
