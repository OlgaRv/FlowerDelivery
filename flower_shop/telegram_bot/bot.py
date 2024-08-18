import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from django.conf import settings
from orders.models import Order


async def start(update: Update, context):
    await update.message.reply_text('Hello! This bot will notify you about new orders.')


async def new_order_notification(order_id):
    # Загружайте детали заказа из базы данных
    order = Order.objects.get(id=order_id)
    message = f"New order from {order.user.email}: {order.product.name} x {order.quantity}, total: {order.total_price}"

    # Отправьте сообщение флористам (всем или по id чатов)
    for chat_id in settings.TELEGRAM_CHAT_IDS:
        await context.bot.send_message(chat_id=chat_id, text=message)


def main():
    app = ApplicationBuilder().token(os.getenv('TELEGRAM_BOT_TOKEN')).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()


if __name__ == '__main__':
    main()
