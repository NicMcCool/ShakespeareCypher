import telegram
from secrets import telegram_token

msg = "INiTi8"
bot = telegram.Bot(token=telegram_token)
status = bot.send_message(
    chat_id="@AphaereseK", text=msg, parse_mode=telegram.ParseMode.HTML
)

print(status)
