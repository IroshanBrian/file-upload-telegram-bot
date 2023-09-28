from typing import final
from telegram import Update
from telegram.ext import Applicationm, CommandHandler, MessageHandler, filters, ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text('Hello! Yuta is at ur service 😀. How can i help you?')
     
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text('Ok i`ll help you')
     
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text('This is custom command')