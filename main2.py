import mouse
import random
import webbrowser
import pyautogui

list1 = list(range(1, 101))

list2 = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
         ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
         '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
         'p', 'q', 'r', 's', 't', 'u', 'v','x', 'y', 'z', '{', '|', '}', '~',
         'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
         'browserback', 'browserfavorites', 'browserforward', 'browserhome',
         'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
         'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
         'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
         'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
         'f21', 'f22', 'f23', 'f24', 'f3', 'f5', 'f6', 'f7', 'f8', 'f9',
         'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
         'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
         'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
         'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
         'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
         'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
         'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
         'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
         'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
         'command', 'option', 'optionleft', 'optionright']

list3 = ['https://www.youtube.com/', 'https://stackoverflow.com/', 'https://twitter.com/' ]

while True:
    
    list1_random = (random.choice(list1))
    list2_random = (random.choice(list2))
    list3_random = (random.choice(list3))
    mouse.move(list1_random, list1_random, absolute=False)
    pyautogui.hotkey('list2_random')
    webbrowser.open(list3_random)
    mouse.click('left')
    mouse.click('middle')
    mouse.click('right')
