from tok import TOKEN
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, filters
from telegram import Update

async def duck_command(update, context):
    try:
        duck = open('assets/duck.mp3', 'rb')
        await update.message.reply_audio(audio=duck)
    except:
        await update.message.reply_text('can\'t quack today')

async def lamb_command(update: Update, context: CallbackContext):
    try:
        lamb = open('assets/lamb.mp3', 'rb')
        await update.message.reply_audio(audio=lamb) #type: ignore 
    except:
        await update.message.reply_text('can\'t mbheee today') #type: ignore


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("duck", duck_command))
app.add_handler(CommandHandler("lamb", lamb_command))
app.run_polling()