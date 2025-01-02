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

cogs_list = [
    'user_cmds',
    'aquarium_cmds',
    'miscellaneous_cmds',
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

# Run the bot with the token
bot.run(token)
