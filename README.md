# EXIF bot

Simple tool to analyze EXIF data of the image

## Deploying your own copy of the bot 

1. Clone repository

```bash
$ git clone git@github.com:ethercod3/EXIF-bot.git
```

2. Install poetry

```bash
$ pip3 install poetry
```

3. Install dependencies

```bash
$ cd EXIF-bot && poetry install 
```

3. Create configuration file

```bash
$ touch .env
```

4. Edit your config

```
BOT_TOKEN=your token
SAVE_TO=directory for user uploads
```

5. Start bot 

```bash
$ poetry run src/bot/main.py
```
