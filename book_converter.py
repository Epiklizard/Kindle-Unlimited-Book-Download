
import pyautogui as pyauto
import time

pyauto.PAUSE = 0.25
print('>>> 5 SECONDS TO CTRL-C <<<')
time.sleep(5)


def convert_book(pages=10):
    x = list(range(0, pages, 2))
    for i in x:
        time.sleep(1)
        if pyauto.pixelMatchesColor(979, 588, (255, 255, 255)):
            '''Left Page Download'''
            pyauto.leftClick(980, 550)
            pyauto.hotkey('ctrl', 'prtsc')
            pyauto.moveTo(210, 135)
            time.sleep(1.1)
            pyauto.dragRel(770, 890, duration=1.3)
            time.sleep(0.5)
            pyauto.hotkey('ctrl', 's')
            time.sleep(1)
            pyauto.typewrite(str(i))
            time.sleep(0.45)
            pyauto.press('enter')

            '''Right Page Download'''
            pyauto.leftClick(980, 550)
            pyauto.hotkey('ctrl', 'prtsc')
            pyauto.moveTo(960, 130)
            time.sleep(1.1)
            pyauto.dragRel(780, 890, duration=1.3)
            time.sleep(0.5)
            pyauto.hotkey('ctrl', 's')
            time.sleep(1)
            pyauto.typewrite(str(i+1))
            time.sleep(0.45)
            pyauto.press('enter')

            '''Next Page'''
            time.sleep(0.75)
            pyauto.rightClick()
            pyauto.press('right')

        else:
            continue


convert_book(300)



