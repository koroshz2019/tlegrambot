from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# جایگزین کردن با توکن ربات شما
TOKEN = "7901413153:AAEsB-wzeyExL88ymuw3jWt8zs8q3KJcDAU"

# دستور start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("سلام! یک عدد ارسال کن تا من یک واحد به آن اضافه کنم.")

# پردازش پیام‌های عددی
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    try:
        number = int(text)
        result = number + 1
        await update.message.reply_text(f"نتیجه: {result}")
    except ValueError:
        await update.message.reply_text("لطفاً فقط یک عدد ارسال کن.")

# تنظیم ربات
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == "__main__":
    main()