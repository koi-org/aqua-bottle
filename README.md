# Aquarium Bot 🐠

Raise and manage your own virtual aquarium full of unique fish directly within Discord! This bot allows users to collect species, feed them, and maintain their aquatic environment.

<p align="center">
  <img src="https://img.shields.io/badge/python-3.11+-blue.svg" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/discord.py-vX.Y.Z-7289DA.svg" alt="discord.py">
  <img src="https://img.shields.io/badge/Supabase-GREEN.svg" alt="Supabase">
</p>

## Table of Contents

- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Configuration](#installation--configuration)
- [Usage (Bot Commands)](#usage-bot-commands)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## About The Project

Aquarium Bot brings a fun and interactive fish-keeping experience to your Discord server. Users can collect different fish species, feed them, manage their aquarium's health, and watch their aquatic pets thrive. It's built using the powerful `discord.py` library and leverages Supabase for persistent data storage, ensuring your aquarium progress is always saved.

## Built With

This project utilizes the following core technologies:

- [Python 3.11+](https://www.python.org/)
- [discord.py](https://discordpy.readthedocs.io/en/latest/) - A modern Python library for the Discord API.
- [Supabase](https://supabase.io/) - An open-source Firebase alternative for database, auth, and realtime subscriptions.

## Getting Started

To get a local copy up and running or to host the bot yourself, follow these steps.

### Prerequisites

- Python 3.11 or newer installed.
- A Discord Bot Token. Learn how to create a bot and get a token from the [Discord Developer Portal](https://discord.com/developers/applications) and [discord.py documentation](https://discordpy.readthedocs.io/en/latest/discord.html).
- A Supabase account and project. You will need your **Project URL** and **`anon` public key** (or `service_role` key if appropriate for your bot's backend logic).

### Installation & Configuration

1.  **Clone the repository:**

2.  **Set up Environment Variables:**
    Create a `.env` file in the project root directory (where your main bot script is) and add your credentials:

    ```env
    DISCORD_TOKEN=your_discord_bot_token_here
    DEFAULT_GUILD=your_supabase_project_url_here
    DATABASE_URI=your_supabase_anon_or_service_key_here
    ```

3.  **Create and Activate Virtual Environment:**

    ```bash
    python3 -m venv venv
    ```

    Activate it:

    - Linux/macOS: `source venv/bin/activate`
    - Windows: `venv\Scripts\activate`

4.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    _(If you add new dependencies later, update your `requirements.txt` with: `pip freeze > requirements.txt`)_

5.  **Run the Bot:**
`bash
    python3 bot.py
    `
<!-- TODO: ADD LATER

## Usage (Bot Commands)

Interact with your aquarium using the following commands. (Default prefix might be `!`, `?`, or as configured).

- **`[prefix]start`** - Creates your very own aquarium if you don't have one.
- **`[prefix]collect`** - Try your luck at collecting a new fish!
- **`[prefix]feed [fish_id/all]`** - Feeds a specific fish or all your fish.
- **`[prefix]view`** - Displays your current aquarium and its inhabitants.
- **`[prefix]shop`** - Shows available items or fish to purchase.
- **`[prefix]help`** - Displays a list of available commands and how to use them.

_[Please replace the above commands, descriptions, and [prefix] with your bot's actual commands and functionality. Be specific!]_ -->
