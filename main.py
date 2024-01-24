from tok import TOKEN
from telegram.ext import ApplicationBuilder, CommandHandler

async def duck_command(update, context):
    try:
        duck = open('assets/duck.mp3', 'rb')
        await update.message.reply_audio(audio=duck)
    except:
        await update.message.reply_text('can\'t quack today')


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("duck", duck_command))
app.run_polling()