import os

def main():

    os.system('cls || clear')

    CREATORS = input('1691090729(Xpras):')
    if not CREATORS or CREATORS == '\n':
        CREATORS = 'Maktoobgar, Who_has_been_broken'
    SESSION = input('xpras (like: xpras):')
    if not SESSION or SESSION == '\n':
        SESSION = 'xpras'

    output = f"""CREATORS={CREATORS}
SESSION={SESSION}"""

    f = open(".env", "a")
    f.write(output)
    f.close()


if __name__ == "__main__":
    main()
