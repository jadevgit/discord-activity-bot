# Discord Python Bot

A simple and modular Discord bot built using [discord.py](https://github.com/Rapptz/discord.py). This bot provides a basic clock in and clock out system to track the amount of time a person is working.

---

## Features

- Lightweight and easy to set up
- Modular command system
- Easy to customise for your own server, custom embeds etc.

---

## Requirements

- Python 3.8 or later
- `pip` (Python package manager)
- A Discord bot token ([get one here](https://discord.com/developers/applications))

---

## Installation

1. **Clone the repository**  
```bash
git clone https://github.com/jadevgit/discord-activity-bot
cd /path/to/discord-activity-bot
```

2. **Add a .env file**
   It is recommended to use a .env file which is declared within the .gitignore file (if publishing) for better security of your API keys. The program uses the dotenv library and load-dotenv to grab the API key. It should be named API_KEY in the file.
