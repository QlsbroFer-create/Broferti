import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔐 Токен беремо із середовища Render
TOKEN = os.getenv("TOKEN")

# 📢 Список каналів
CHANNELS = [
    "https://t.me/vxakFvINa3CSOOsy",
    "https://t.me/2smSi4WNYn0DjY",
    "https://t.me/W0dA80_gWEhG0D2L",
    "https://t.me/WhsK8FbNd-jPJ6MEy"
]

# 🌟 Основний канал
MAIN_CHANNEL = "https://t.me/+tAhvPb6r3Jx3NGIy"


# 🚀 Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(f"✅ Підписатися на канал {i+1}", url=url)]
        for i, url in enumerate(CHANNELS)
    ]
    keyboard.append([InlineKeyboardButton("☑️ Я підписався", callback_data="done")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привіт 👋!\n"
        "Підпишись на всі канали та натисни ☑️ 'Я підписався', щоб отримати доступ.",
        reply_markup=reply_markup
    )


# ✅ Обробка кнопки “Я підписався”
async def check_done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        f"Дякую ❤️! Ось головний канал:\n👉 {MAIN_CHANNEL}"
    )


# ⚙️ Основна функція запуску
async def main():
    print("🚀 Запуск Telegram-бота...")
    if not TOKEN:
        raise ValueError("❌ Токен не знайдено! Додай змінну TOKEN у Render Environment.")

    # Створюємо застосунок
    app = Application.builder().token(TOKEN).build()

    # Обробники команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_done, pattern="done"))

    print("✅ Бот працює! Готовий приймати команди.")
    await app.run_polling(close_loop=False)


if  __name__ == "__main__":
    asyncio.run(main())
