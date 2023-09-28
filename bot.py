from typing import final
from telegram import Update
from telegram.ext import Applicationm, CommandHandler, MessageHandler, filters, ContextTypes


# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text('Hello! Yuta is at ur service 😀. How can i help you?')
     
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text('Ok i`ll help you')
     
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text('This is custom command')
     
# responses

def handle_responses(text: str)-> str:
     processed: str = text.lower()
     
     if 'hello' in text:
          return 'Hey There!'
     if 'hi' in text:
          return 'Hey There!'
     if 'hey' in text:
          return 'Hey There!'
     return 'I can`t understand'