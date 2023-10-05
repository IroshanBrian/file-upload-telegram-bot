import os
from typing import final
import logging
import time
from telegram import Update, InputFile
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    CallbackContext,
)
from dotenv import load_dotenv
from colorama import Fore


# ----------------------------------------LOGS---------------------------------------------#

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)



# ----------------------------------------CONFIG---------------------------------------------#
load_dotenv()
TOKEN = os.getenv("Token")
UPLOAD_DIR = os.getenv("FOLDER_DIR")


# ----------------------------------------FUNCTIONS---------------------------------------------#
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Type /help to see how can i help you?"
    )
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Here are the commands you can use:\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/list- List of the files in the folder\n"
        "/download - Download a file from the bot\n"
        "/downloadAll - Download all files in the folder\n"
    )


async def send_list_of_files(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    folder_path = UPLOAD_DIR
    files_list = os.listdir(folder_path)
    files_list_message = 'List of files in the folder:\n\n' + '\n'.join(files_list)
    await context.bot.send_message(chat_id=chat_id, text=files_list_message)

async def list_of_files(update: Update, context: CallbackContext) -> None:
    await send_list_of_files(update, context)



async def download_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    folder_path = UPLOAD_DIR
    chat_id = update.message.chat_id

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                await context.bot.send_document(chat_id,document=f,read_timeout=60, write_timeout=60, connect_timeout=60, pool_timeout=60)
                time.sleep(5)

async def downloadSpecific_command(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    file_name = update.message.text.split(" ", 1)[1]
    file_path = f"{UPLOAD_DIR}/{file_name}"

    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            await update.message.reply_document(document=file,read_timeout=60, write_timeout=60, connect_timeout=60, pool_timeout=60)
    else:
        await update.message.reply_text("File not found.")

# ----------------------------------------RESPONSES---------------------------------------------#
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if "hello" in text:
        return "Hey There!"
    if "hi" in text:
        return "Hey There!"
    if "hey" in text:
        return "Hey There!"
    return "I can`t understand"

# ----------------------------------------CHAT TYPE---------------------------------------------#
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    await update.message.reply_text(f'Use /help to get command panel')
    print( Fore.YELLOW + f'{update.message.chat.full_name} ({update.message.chat.id}) in {message_type}: "{text}"' + Fore.GREEN)


    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            response: str = handle_response(text)

        print("Bot:", response)
        await update.message.reply_text(response)


# ----------------------------------------ERROR HANDLING---------------------------------------------#
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(Fore.RED + f"Caused error : {context.error}" + Fore.GREEN)


if __name__ == "__main__":
    app = Application.builder().token(TOKEN).connect_timeout(60).pool_timeout(60).read_timeout(60).write_timeout(60).get_updates_read_timeout(42).build()

# ----------------------------------------TG_COMMANDS---------------------------------------------#
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("list", list_of_files))
    app.add_handler(CommandHandler("download", downloadSpecific_command))
    app.add_handler(CommandHandler("downloadAll", download_command))
    app.add_handler(CommandHandler("chat", handle_message))

    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # errors
    app.add_error_handler(error)

# ----------------------------------------POLLING---------------------------------------------#
    print(Fore.BLUE + "Bot is running.." + Fore.GREEN)
    app.run_polling(poll_interval=10)
