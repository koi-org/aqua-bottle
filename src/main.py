import discord
import os  # default module
from dotenv import load_dotenv
from manager import Manager
from user import User

# Load environment variables from the .env file
load_dotenv()

# Retrieve the bot token from the environment
token = os.getenv("DISCORD_TOKEN")

# Check if the token exists
if not token:
    raise ValueError("DISCORD_TOKEN is not set in the .env file.")

# Initialize the bot
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot", guild_ids=[692964332643942463])
async def hello(ctx: discord.ApplicationContext):
    username = ctx.author.name
    user_id = ctx.author.id
    channel_id = ctx.channel.id
    channel_name = ctx.channel.name
    guild_id = ctx.guild.id

    await ctx.respond(f"Hello {username} (User ID: {user_id})! You are in channel {channel_name} (ID: {channel_id}). (Guild id: {guild_id})")

@bot.slash_command(name="greeting", description="greeting", guild_ids=[692964332643942463])
async def greeting(ctx: discord.ApplicationContext):
    await ctx.respond(f"Greetings {ctx.author.name}!")

@bot.slash_command(name="register", description="Register your account for the aquarium game!", guild_ids=[692964332643942463])
async def register(ctx: discord.ApplicationContext, username: str = None):
    discord_name = ctx.author.name
    user_id = ctx.author.id

    if not username:
        username = discord_name

    if Manager.add_user(user_id, username):
        await ctx.respond(f"{discord_name} has successfully registered for the game as: {username}.")
    else:
        await ctx.respond(f"You're already in the game.")

@bot.slash_command(name="create_aquarium", description="Create your own aquarium with your registered account!", guild_ids=[692964332643942463])
async def create_aquarium(ctx: discord.ApplicationContext, name: str):
    user_id = ctx.author.id
    user = Manager.get_user(user_id)

    if user is None:
        await ctx.respond("You are not a valid user, please register before creating an aquarium!")
    else:
        # Add logic to create the aquarium
        await ctx.respond(f"Aquarium '{name}' has been successfully created!")


# Run the bot with the token
bot.run(token)
