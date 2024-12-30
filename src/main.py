import discord
import os  # default module
from dotenv import load_dotenv

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
    # Get user info
    username = ctx.author.name
    user_id = ctx.author.id
    # Get channel info
    channel_id = ctx.channel.id
    channel_name = ctx.channel.name

    # Respond with a custom message including the user's name, ID, channel ID, and channel name
    await ctx.respond(f"Hello {username} (User ID: {user_id})! You are in channel {channel_name} (ID: {channel_id}).")

# Run the bot with the token
bot.run(token)
