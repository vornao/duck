from tok import TOKEN
from telegram.ext import ApplicationBuilder, CommandHandler

try:
    duck = open('assets/duck.mp3', 'rb')
except Exception as e:
    print(e)
    exit()

async def duck_command(update, context):
    await update.message.reply_audio(audio=duck)


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("duck", duck_command))
app.run_polling()