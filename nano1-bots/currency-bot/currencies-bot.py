import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, JobQueue
from utils.currencies import get_currncies_string_format



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define your bot's token
TOKEN = '7079042536:AAH4GLDJcJhNFdjGZvyAxWHRXCXwyw4c0z0'
CHANNEL_ID = '@innofinitybotnews'  # Replace with your channel ID or username
MESSAGE = "لیست قیمت‌ها:\n"

# Define the function that sends the periodic message
def send_periodic_message(context: CallbackContext):
    context.bot.send_message(chat_id=CHANNEL_ID, text=MESSAGE+get_currncies_string_format())

# Main function to start the bot
def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN, use_context=True)

    # Get the JobQueue
    job_queue = updater.job_queue

    # Schedule the job every 10 seconds (can change the interval as needed)
    job_queue.run_repeating(send_periodic_message, interval=10, first=10)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()