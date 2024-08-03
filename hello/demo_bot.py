import requests
import telebot
import schedule
import time
#import datetime

# Telegram bot Token 
BOT_TOKEN = '7442765865:AAGGiJMEXJ7HXnMFKN_ZN4CjD4dEn3wxRXI'

# Telegram Channel ID
CHANNEL_ID = '@EntraCodeChannel'

bot = telebot.TeleBot(BOT_TOKEN)

def get_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False
    }
    response = requests.get(url, params)
    return response.json()

def format_message(data):
    message = "Top 10 Cryptocurrencies:\n\n"
    for coin in data:
        message+= f"{coin['name']} ({coin['symbol'].upper()}):\n"
        message+= f"Price: ${coin['current_price']:,.2f}\n"
        message+= f"24h Change: {coin['price_change_percentage_24h']:.2f}%\n\n"
    return message

def show_coin_list():
    try:
        data = get_crypto_data()
        message = format_message(data)
        bot.send_message(CHANNEL_ID, message)
        #print(message)
    except Exception as e:
        print(f"Error: {e}")

# Schedule the Update to run every hour
schedule.every().hour.do(show_coin_list)

# Run the bot
while True:
    schedule.run_pending()
    time.sleep(1)