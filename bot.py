import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot online!\n\n"
        "Comandos disponíveis:\n"
        "/start - Iniciar\n"
        "/status - Verificar estado"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 Bot funcionando normalmente.")

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN não configurado.")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    print("Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
