import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio

# Токен з Render (Environment Variable)
TOKEN = os.getenv("TOKEN")

# Список каналів
CHANNELS = [
    "https://t.me/+vaxfVihm3C05ODYy",
    "https://t.me/+2mRsSn0SWUYyNDUy",
    "https://t.me/+OW0A0_gW6EthODZi",
    "https://t.me/+WwsK8FNhJ-pjMGEy"
]

# Основний канал
MAIN_CHANNEL = "https://t.me/+tIahvP6bf3xjNGIy"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /start"""
    keyboard = [
        [InlineKeyboardButton(f"{i+1}️⃣ Підписатися на канал", url=url)]
        for i, url in enumerate(CHANNELS)
    ]
    keyboard.append([InlineKeyboardButton("✅ Я підписався", callback_data="done")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привіт! 👋\n\nПідпишись на всі канали і натисни '✅ Я підписався', щоб отримати доступ.",
        reply_markup=reply_markup
    )


async def check_done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Кнопка '✅ Я підписався'"""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"🎉 Дякую! Ось головний канал:\n{MAIN_CHANNEL}")


async def main():
    """Основна функція запуску"""
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_done, pattern="done"))

    print("✅ Бот запущено і працює...")
    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
