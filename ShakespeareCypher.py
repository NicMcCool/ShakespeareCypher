import random, string, base64, string


def open_text_file(filename):
    with open(filename, "r") as f:
        for index, line in enumerate(f):
            current_line = "Line {}: {}".format(index, line.strip()).encode()
            encode_line = codecs.encode(str(base64.b64encode(current_line)), "rot_13")
            random_two = "".join(random.choices(string.ascii_lowercase, k=2))
            encode_line = encode_line.replace("o'", random_two)
            encode_line = encode_line.replace("==", ":)")
            fill_chars = "".join(
                random.choices(
                    string.ascii_letters + string.digits, k=140 - len(encode_line)
                )
            )
            print(encode_line + fill_chars)


open_text_file("S:\Dropbox\Tech\GitHub\ShakespeareCypher\AWTEW.txt")
