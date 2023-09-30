import os
from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv('Token')
BOT_USERNAME = os.getenv("BOT_USERNAME")


# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text('Hello! Yuta is at ur service 😀. How can i help you?')
     
async def pic_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_video('1.mp4')
     
# responses
def handle_response(text: str)-> str:
     processed: str = text.lower()
     
     if 'hello' in text:
          return 'Hey There!'
     if 'hi' in text:
          return 'Hey There!'
     if 'hey' in text:
          return 'Hey There!'
     return 'I can`t understand'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
     message_type: str = update.message.chat.type
     text: str = update.message.text
     
     print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
     
     # group mention replies
     if message_type == 'group':
          if BOT_USERNAME in text:
               new_text: str = text.replace(BOT_USERNAME, '').strip()
               response: str = handle_response(new_text)
          else:
               response: str = handle_response(text)
          
          print('Bot:', response)
          await update.message.reply_text(response)

# error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
     print(f'Update {update} caused error {context.error}')
     
if __name__ == '__main__':
     app = Application.builder().token(TOKEN).build()
     
     # commands
     app.add_handler(CommandHandler('start', start_command))
     app.add_handler(CommandHandler('pic', pic_command))
     
     # messages
     app.add_handler(MessageHandler(filters.TEXT, handle_message))
     
     
     # errors
     app.add_error_handler(error)
     
     # polls the bot
     print('Polling...')
     app.run_polling(poll_interval=3)
     