import random, string, base64, codecs, time, telegram
from random import randint
from secrets import telegram_token, path_to_text



def open_text_file(filename):
    bot = telegram.Bot(token=telegram_token)
    with open(filename, "r") as f:
        for index, line in enumerate(f):
            current_line = "Line {}: {}".format(index, line.strip()).encode()
            encode_line = codecs.encode(str(base64.b64encode(current_line)), "rot_13")
            encode_line = encode_line.replace("'", "!")
            encode_line = encode_line.replace("==", ":)")
            fill_chars = "".join(
                random.choices(
                    string.ascii_letters + string.digits, k=132 - len(encode_line)
                )
            )
            msg = encode_line + fill_chars + "#AWTEW"
            status = bot.send_message(
                chat_id="@AphaereseK", text=msg, parse_mode=telegram.ParseMode.HTML
            )
            print(status)
            time.sleep(randint(7200, 86400))


open_text_file(path_to_text)
