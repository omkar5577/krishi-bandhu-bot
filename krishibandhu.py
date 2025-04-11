from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

# Replace this with your bot token
TOKEN = '7291462264:AAFb3_wycd2R3fi0TqAoVZxy_t8WLiTrEHE'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to *Krishi Bandhu – Green Pulse*!\n"
        "I’m your farming assistant. Ask me anything about agriculture!",
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "*Krishi Bandhu – Green Pulse Help Menu*\n\n"
        "Use the following commands:\n"
        "/start – Welcome message\n"
        "/help – Show this help menu\n"
        "Just type your farming-related question to get help!",
        parse_mode='Markdown'
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running as Krishi Bandhu – Green Pulse...")
    app.run_polling()

if __name__ == '__main__':
    main()
