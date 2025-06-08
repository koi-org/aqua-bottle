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
                    await cursor.execute('insert into "Users" (id, username, currency) values (%s, %s, %s)',
                                   (user_id, username, 1000))
                    await conn.commit()
                    return_status = "User successfully registered!"
                except UniqueViolation:
                    return_status = "User already exists"
                except Exception as e:
                    # debugging
                    print("Error: ", e)
                    return_status = "An internal error occurred. Please try again later."

        await interaction.response.send_message(return_status)

    @user.command(name="profile", description="Show user profile and currency info")
    async def profile(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        username = interaction.user.name  # Or pull from DB if custom name
        currency = 0  # Default fallback, or pull from DB

        async with self.bot.db.connection() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(
                    'SELECT username, currency FROM "Users" WHERE id = %s',
                    (user_id,)
                )
                result = await cursor.fetchone()
                if result:
                    username, currency = result

        # Create the embed
        embed = discord.Embed(
            title="User Profile",
            description="Here’s your current info:",
            color=discord.Color.og_blurple()
        )
        embed.add_field(name="Username", value=f"`{username}`", inline=False)
        embed.add_field(name="Currency", value=f"`{currency}` coins", inline=False)
        embed.set_thumbnail(url=interaction.user.display_avatar.url)
        embed.set_footer(text="aqua bottle")

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(User(bot, bot.db))
