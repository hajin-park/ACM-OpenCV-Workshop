import keyboard as kb
from time import sleep
from modules.windowcapture import WindowCapture

sct = WindowCapture()

kb.wait('s')  # start the bot with a "s" keypress
print("working")


def main():
    sct.run()
    while sct.screenshot is None:  # wait for the first screenshot, prevents errors
        sleep(0)
    print("working2")

    while True:
        sct.update([[0, 0, 100, 100], [0, 0, 50, 50]])
        sct.run()
        if kb.is_pressed('q'):  # terminate the bot with a "q" keypress
            sct.stop()
            break
        print("working3")


if __name__ == "__main__":
    main()
