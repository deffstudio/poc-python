import os 
from dotenv import load_dotenv
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Load environment variables from the .env file
load_dotenv()

# Get the bot token from the .env file
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)

# Start command
@bot.message_handler(commands=['start'])

def start_command(message):
    ''' Start command '''
    bot.reply_to(message, "Hello! Welcome to the Axera101 bot!")
    send_menu(message)

# Help command

@bot.message_handler(commands=['help'])

def help_command(message):
    ''' Help command '''
    bot.reply_to(message, "To use the Axera101 bot, you can send me a list of commands. Here are some useful ones:\n\n/start - Start the bot\n/help - Get help with the bot\n/inventory - Display your inventory\n/status - Check your current status\n/fight - Start a battle with a random enemy")

# Send menu
def send_menu(message):
    ''' Function to setup the menu'''
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Buy", callback_data="buy"),
                    InlineKeyboardButton("Sell", callback_data="sell"),
                    InlineKeyboardButton("Settings", callback_data="settings"),
                    InlineKeyboardButton("Withdraw", callback_data="withdraw")
    )
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

# Back to menu button
def send_back_to_menu(chat_id):
    ''' Function to go back to the menu'''
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Back to menu", callback_data="back_to_menu"))
    bot.send_message(chat_id, "Choose an action:", reply_markup=markup)

# Handle button presses

@bot.callback_query_handler(func=lambda call: True)

def callback_query(call):
    ''' Handle button presses'''
    if call.data == "buy":
        # Add buy logic here
        bot.answer_callback_query(call.id, "You selected Buy.")
        bot.send_message(call.message.chat.id, "You selected Buy.")
        send_back_to_menu(call.message.chat.id)
    elif call.data == "sell":
        # Add sell logic here
        bot.answer_callback_query(call.id, "You selected Sell.")
        bot.send_message(call.message.chat.id, "You selected Sell.")
        send_back_to_menu(call.message.chat.id)
    elif call.data == "settings":
        # Add settings logic here
        bot.answer_callback_query(call.id, "You selected Settings.")
        bot.send_message(call.message.chat.id, "You selected Settings.")
        send_back_to_menu(call.message.chat.id)
    elif call.data == "withdraw":
        # Add withdraw logic here
        bot.answer_callback_query(call.id, "You selected Withdraw.")
        bot.send_message(call.message.chat.id, "You selected Withdraw.")
        send_back_to_menu(call.message.chat.id)
    elif call.data == "back_to_menu":
        # Go back to the main menu
        bot.answer_callback_query(call.id, "Returning to main menu...")
        send_menu(call.message)



# Start the bot

if __name__ == "__main__":
    bot.polling()