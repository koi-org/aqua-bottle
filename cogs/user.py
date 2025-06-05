import discord
from discord.ext import commands


class User(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @discord.app_commands.command(name="register", description="Registers user!")
    async def register(self, interaction: discord.Interaction, input_name:str=''):
        user_id = str(interaction.user.id)
        # User can choose their name, their default name would be their username.
        username = input_name if input_name else str(interaction.user)
        return_status = "Registered!"

        async with self.bot.db.connection() as conn:
            async with conn.cursor() as cursor:
                try:
                    await cursor.execute('insert into "Users" (id, username) values (%s, %s)',
                                   (user_id, username,))
                    await conn.commit()
                    # debugging
                    print("User successfully registered!")
                except Exception as e:
                    error_string = "User already exists"
                    # debugging
                    print("Error: ", e)
                    return_status = error_string

        await interaction.response.send_message(return_status)


async def setup(bot):
    await bot.add_cog(User(bot, bot.db))
