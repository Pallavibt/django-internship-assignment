import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internship_project.settings")
django.setup()

import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from decouple import config
from core.models import TelegramUser
from asgiref.sync import sync_to_async

@sync_to_async
def save_user(username, telegram_id):
    obj, created = TelegramUser.objects.get_or_create(
        username=username,
        defaults={'telegram_id': telegram_id}
    )
    return created

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.username

    # Fallback for users with no username
    if not username:
        username = f"{user.first_name or 'user'}_{user.id}"

    telegram_id = user.id

    await save_user(username, telegram_id)

    await update.message.reply_text(f"Hello, {username}! You're now registered.")

def main():
    token = config("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
