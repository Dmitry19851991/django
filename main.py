# main.py
import telebot
from extensions import CurrencyConverter, APIException
import config

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    instructions = (
        "Привет! Я бот для получения курса валют. Используй команду /values, чтобы узнать доступные валюты.\n"
        "Для получения цены введи: <валюта1> <валюта2> <количество>\n"
        "Пример: USD EUR 100"
    )
    bot.send_message(message.chat.id, instructions)


@bot.message_handler(commands=['values'])
def handle_values(message):
    available_currencies = "Доступные валюты: USD, EUR, RUB"
    bot.send_message(message.chat.id, available_currencies)


@bot.message_handler(func=lambda message: True)
def handle_currency_conversion(message):
    try:
        input_data = message.text.split()
        if len(input_data) != 3:
            raise APIException("Неправильный формат ввода. Используйте: <валюта1> <валюта2> <количество>")

        base_currency, quote_currency, amount = input_data
        amount = float(amount)

        result = CurrencyConverter.get_price(base_currency, quote_currency, amount)
        bot.send_message(message.chat.id, f"{amount} {base_currency} = {result} {quote_currency}")

    except APIException as e:
        bot.send_message(message.chat.id, f"Ошибка: {e.message}")


if __name__ == "__main__":
    bot.polling(none_stop=True)
