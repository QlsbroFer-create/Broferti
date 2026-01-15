import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Токен беремо з Environment Variables Render
TOKEN = os.getenv("TOKEN")

CHANNELS = [
    "https://t.me/+vaxfVihm3C05ODYy",
    "https://t.me/+2mRsSn0SWUYy",
    "https://t.me/+OW0A0_gW6EthODZi",
    "https://t.me/+WwsK8FNhJ-pjMGEy"
]

MAIN_CHANNEL = "https://t.me/+tIahvP6bf3xjNGIy"

def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton(f"{i+1}️⃣ Підписатися на канал", url=url)] for i, url in enumerate(CHANNELS)]
    keyboard.append([InlineKeyboardButton("✅ Я підписався", callback_data="done")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Привіт! 👋\n\nПідпишись на всі канали і натисни '✅ Я підписався', щоб отримати доступ.",
        reply_markup=reply_markup
    )

def check_done(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(f"🎉 Дякую! Ось головний канал:\n{MAIN_CHANNEL}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(check_done, pattern="done"))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()