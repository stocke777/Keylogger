from pynput import keyboard
from pynput.keyboard import Key

# write to demofile2
def writefile(k):
    f = open("demofile2.txt", "a")
    f.write(k)
    f.close()

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        writefile(key.char)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        if key == Key.space:
            writefile(" da ")

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
