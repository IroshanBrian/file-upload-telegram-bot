import os
from typing import final
import logging
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


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

load_dotenv()


TOKEN = os.getenv("Token")
BOT_USERNAME = os.getenv("BOT_USERNAME")
UPLOAD_DIR = "./files/"


# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Yuta is at ur service 😀. How can i help you?"
    )


async def download_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_name = update.message.text.split(" ", 1)[1]
    file_path = f"{UPLOAD_DIR}/{file_name}"

    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            await update.message.reply_document(document=file)
    else:
        await update.message.reply_text("File not found.")


# responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if "hello" in text:
        return "Hey There!"
    if "hi" in text:
        return "Hey There!"
    if "hey" in text:
        return "Hey There!"
    return "I can`t understand"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # group mention replies
    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            response: str = handle_response(text)

        print("Bot:", response)
        await update.message.reply_text(response)


# error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("sendme", download_command))

    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # errors
    app.add_error_handler(error)

    # polls the bot
    print("Polling...")
    app.run_polling(poll_interval=3)
