import os
from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

TOKEN = os.getenv("TELEGRAM_TOKEN")

def start(update, context):
    update.message.reply_text("مرحبًا بك 👋\nأرسل لي اسم زوج العملة أو الذهب لتحصل على التحليل.")

def handle_message(update, context):
    text = update.message.text
    if "gold" in text.lower() or "ذهب" in text:
        response = "🔎 تحليل الذهب:\nالهدف 2350\nالشراء من منطقة 2300\nوقف الخسارة 2280"
    else:
        response = f"📊 تحليل {text}:\nحاليًا لا توجد فرصة قوية. نتابع الاتجاهات."
    update.message.reply_text(response)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
