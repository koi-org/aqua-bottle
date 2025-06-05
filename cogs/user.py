import discord
from discord.ext import commands
from psycopg.errors import UniqueViolation

class User(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    user = discord.app_commands.Group(name="user", description="...")

    @user.command(name="register", description="Registers user!")
    async def register(self, interaction: discord.Interaction, input_name:str=''):
        user_id = str(interaction.user.id)
        # User can choose their name, their default name would be their username.
        username = input_name if input_name else str(interaction.user)
        return_status = "Unexpected error occured"

        async with self.bot.db.connection() as conn:
            async with conn.cursor() as cursor:
                try:
                    await cursor.execute('insert into "Users" (id, username) values (%s, %s)',
                                   (user_id, username,))
                    await conn.commit()
                    return_status = "User successfully registered!"
                except UniqueViolation:
                    return_status = "User already exists"
                except Exception as e:
                    # debugging
                    print("Error: ", e)

        await interaction.response.send_message(return_status)


async def setup(bot):
    await bot.add_cog(User(bot, bot.db))
