import os
from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

TOKEN = os.getenv("TELEGRAM_TOKEN")

def start(update, context):
    update.message.reply_text("مرحبًا، أنا بوت الذكاء الاصطناعي علي آي. أرسل لي زوج العملة أو الذهب للتحليل.")

def handle_message(update, context):
    text = update.message.text
    # تحليل بسيط تجريبي
    if "gold" in text.lower() or "ذهب" in text:
        response = "🔎 تحليل الذهب:
الاتجاه صاعد، منطقة الشراء عند 2300، الهدف 2350، وقف الخسارة 2280."
    else:
        response = f"📊 تحليل {text}:
الاتجاه جانبي. لا توجد فرصة قوية حالياً."
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