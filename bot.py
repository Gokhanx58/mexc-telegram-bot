import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Buraya kendi API anahtarlarını gir
MEXC_API_URL = "https://api.mexc.com/api/v3/ticker/price?symbol="
TELEGRAM_BOT_TOKEN = "AAE5bYGqjA6R8tWGUtbl9acH4g3RhcYSyBc"

# Telegram botunun komutları
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("📈 KRİPTO ÇOBANI Trade Bot'a hoş geldin!\nBir işlem çifti girerek analiz alabilirsin.\nÖrnek: /price BTCUSDT")

def get_price(update: Update, context: CallbackContext) -> None:
    if not context.args:
        update.message.reply_text("Lütfen bir işlem çifti girin! Örnek: /price BTCUSDT")
        return

    symbol = context.args[0].upper()
    response = requests.get(MEXC_API_URL + symbol)

    if response.status_code == 200:
        price_data = response.json()
        update.message.reply_text(f"🔹 {symbol} Fiyatı: {price_data['price']} USDT")
    else:
        update.message.reply_text("⚠️ Geçersiz işlem çifti veya MEXC API hatası!")

# Telegram botunu başlat
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("price", get_price))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

