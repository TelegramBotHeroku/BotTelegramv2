import os


def main():
    os.system('cls || clear')

    api_id = input('2389796')
    if not api_id or api_id == '\n':
        api_id = ''
    api_hash = input('b8b23c77ac286a14a41046ea2b66263c')
    if not api_hash or api_hash == '\n':
        api_hash = ''
    bot_token = input('1721959350:AAF1BfS4HY3qEeWnZOOVmzPVZCT5SJ7beCw')
    if not bot_token or bot_token == '\n':
        bot_token = ''

    output = f"""[pyrogram]
api_id = {api_id}
api_hash = {api_hash}
bot_token = {bot_token}"""

    f = open("config.ini", "w")
    f.write(output)
    f.close()


if __name__ == "__main__":
    main()
