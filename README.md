# Files upload from server to telegram


## Requirements

[![](https://camo.githubusercontent.com/cc498548db376c421cdb164e2480f2a88f0625329356cbb6510f15cab7a73337/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666c6174266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534)](https://www.python.org/downloads/) (Version 3.10.12 Works Flawlessly)
## Installation

To deploy this project run

```bash
sudo apt update && apt upgrade
```
```bash
git clone https://github.com/IroshanBrian/file-upload-telegram-bot
```
```bash
cd file-upload-telegram-bot
```
```bash
pip3 install -r requirements.txt
```
## Configuration

You have to configure the `example.env` 

- `Token= !Your telegram bot token`
- `FOLDER_DIR=!Your server folder path`

file and rename it to `.env`

## Usage
 Run the python file
```bash
python3 main.py
```
In the telegram chat use this commands:

- `/start - Start the bot`
- `/help - Show this help message`
- `/list- List of the files in the folder`
- `/download - Download a file from the bot`
- `/downloadAll - Download all files in the folder`


## Documentation

[Python-Telegram-Bot](https://docs.python-telegram-bot.org/en/v20.6/#)

## Credits

- [@PTB](https://github.com/python-telegram-bot/python-telegram-bot)

## Support

For support, email dev.iroshanbrian@gmail.com.
