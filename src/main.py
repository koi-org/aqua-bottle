import discord
import os  # default module
from dotenv import load_dotenv
from user_manager import UserManager
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

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    username = ctx.author.name
    user_id = ctx.author.id
    channel_id = ctx.channel.id
    channel_name = ctx.channel.name

    await ctx.respond(f"Hello {username} (User ID: {user_id})! You are in channel {channel_name} (ID: {channel_id}).")

@bot.slash_command(name="register", description="Register your account for the aquarium game!")
async def register(ctx: discord.ApplicationContext, name: str = None):
    username = ctx.author.name
    user_id = ctx.author.id

    if name and len(name) > 1:
        username = name

    if UserManager.add_user(user_id, username):
        await ctx.respond(f"{username} has successfully registered for the game.")
    else:
        await ctx.respond(f"You're already in the game, {username}")

# Run the bot with the token
bot.run(token)
