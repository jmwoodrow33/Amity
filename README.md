# Amity

A multipurpose Discord bot built using the `discord.ext` commands extension.

## Introduction

This bot is set up to use cogs, which are essentially a collection of commands under a common theme. Cogs are useful for managing your commands and listeners, as it allows you to split your bot commands into separate files and manage them more easily.

As of now, the bot includes a basic ping command that tells the latency.

## Features

- **Command Prefix**: Use `!!` before any command to interact with the bot.
- **Ping Command**: Check the latency between the bot and the server using `!!ping`.
- **Cog System**: Modular design that makes it easy to expand the bot's capabilities.

## Installation & Usage

Ensure you have the `discord.py` library installed.

In the command prompt...
- pip install discord.py
- git clone https://github.com/jmwoodrow33/Amity.git
- cd path-to-discordbot-folder

Set up a config.py file in your project directory with the following format:
TOKEN = "YOUR_DISCORD_BOT_TOKEN"

Then run the bot through the command prompt (python <main_file_name>.py)

## Adding Cogs
To add a new cog:

- Create a new .py file inside the cogs folder.
- Define your commands within a class that inherits from commands.Cog.
- Add a setup function at the bottom of your cog file.
- The bot will automatically detect and load new cogs when restarted.

## Technology Stack
Python
discord.py

## Contributing
Contributions are welcome! Feel free to submit a pull request.

## License
MIT License.

## Contact
John-Michael Woodrow jmwoodrow33@outlook.com

## Acknowledgements
discord.py


