import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler,
    CallbackQueryHandler, ContextTypes
)

# Отримуємо токен із змінних середовища
TOKEN = os.getenv("TOKEN")

# Список каналів, на які потрібно підписатися
CHANNELS = [
    "https://t.me/+vaxfVihm3C05ODYy",
    "https://t.me/+2mRsSn0SWUYyNDUy",
    "https://t.me/+OW0A0_gW6EthODZi",
    "https://t.me/+WwsK8FNhJ-pjMGEy"
]

# Основний канал
MAIN_CHANNEL = "https://t.me/+2eELL_nHMMo1MWRi"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(f"✅ Підписатися на канал {i+1}", url=url)]
        for i, url in enumerate(CHANNELS)
    ]
    keyboard.append([InlineKeyboardButton("☑️ Я підписався", callback_data="done")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Привіт!\nПідпишись на всі канали нижче, а потім натисни «☑️ Я підписався», щоб отримати доступ:",
        reply_markup=reply_markup
    )

# Обробка натискання "Я підписався"
async def check_done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        f"🎉 Дякую! Тепер можеш перейти в головний канал:\n👉 {MAIN_CHANNEL}"
    )

# Основна функція
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_done, pattern="done"))

    print("✅ Бот запущено і він працює!")
    app.run_polling()

if __name__ == "__main__":
    main()
