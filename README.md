<h1>Subjects Bot<img src=".readme/logo.png" align="right"></h1>

[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fatrox%2Fsync-dotenv%2Fbadge&style=flat&label=Tests&logo=_)](https://github.com/victorbnl/subjects-bot/actions/workflows/pytest.yml)

Discord bot for the french server *Un sujet par jour*.

> **Warning**  
> This bot is designed for the french language and probably won't work as expected with other languages due to its inflections engine

# Run

- Install the dependencies: `pip install -r requirements.txt`
- Copy the files from the `samples/` folder and
    - Set the required variables in `.env`
    - Complete `data/config.yml`
- Run the bot: `python3 -m subjects_bot`
