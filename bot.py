import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Отримуємо токен з Render (Environment Variable)
TOKEN = os.getenv("TOKEN")

# Список каналів, на які треба підписатись
CHANNELS = [
    "https://t.me/vxakFvINa3CSOOsy",
    "https://t.me/2smSi4WNYn0DjY",
    "https://t.me/W0dA80_gWEhG0D2L",
    "https://t.me/WhsK8FbNd-jPJ6MEy"
]

# Основний канал
MAIN_CHANNEL = "https://t.me/+tAhvPb6r3Jx3NGIy"


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for i, url in enumerate(CHANNELS):
        keyboard.append([InlineKeyboardButton(f"✅ Підписатися на канал {i+1}", url=url)])
    keyboard.append([InlineKeyboardButton("☑️ Я підписався", callback_data="done")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привіт! 👋\nПідпишись на всі канали й натисни ☑️ 'Я підписався', щоб отримати доступ.",
        reply_markup=reply_markup
    )


# Обробка кнопки "Я підписався"
async def check_done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"Дякую! ❤️ Ось головний канал:\n👉 {MAIN_CHANNEL}")


# Основна функція запуску
async def main():
    print("🚀 Бот запускається...")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_done, pattern="done"))

    print("✅ Бот запущений і працює!")
    await app.run_polling()


# Запуск бота
if name == "main":
    asyncio.run(main())
