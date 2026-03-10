import requests
from telegram.ext import Application, MessageHandler, filters
from backend.config import TELEGRAM_BOT_TOKEN

API_URL = "https://fitness-coach-agent.onrender.com/chat"

async def handle_message(update, context):

    user_id = str(update.message.from_user.id)
    message = update.message.text

    # Send user message to backend
    response = requests.post(
        API_URL,
        json={
            "user_id": user_id,
            "message": message
        }
    )

    reply = response.json()["reply"]

    await update.message.reply_text(reply)


def main():

    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("Telegram bot running...")

    app.run_polling()


if __name__ == "__main__":
    main()