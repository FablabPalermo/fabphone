import time
import digitalio
import board
import adafruit_matrixkeypad
from pynput.keyboard import Key, Controller
import os
keyboard = Controller()




#FabLab raspi
rows = [digitalio.DigitalInOut(x) for x in (board.D26, board.D19, board.D13, board.D6)]
cols = [digitalio.DigitalInOut(x) for x in (board.D5, board.D21, board.D20, board.D16)]


keys = ((1, 2, 3,'A'),
        (4, 5, 6,'B'),
        (7, 8, 9,'C'),
        ('*', 0, '#','D'))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

os.system('mpg123 ~/fabphone/voip/audio/start.mp3 &')
time.sleep(1)


while True:
    keys = keypad.pressed_keys
    #if keys:
    #    print(keys)
    if keys == [1]:
        keyboard.press('1')
        keyboard.release('1')
        os.system('mpg123 ~/fabphone/voip/audio/1.mp3 &')
        time.sleep(0.5)
    if keys == [2]:
        keyboard.press('2')
        keyboard.release('2')
        os.system('mpg123 ~/fabphone/voip/audio/2.mp3 &')
        time.sleep(0.5)
    if keys == [3]:
        keyboard.press('3')
        keyboard.release('3')
        os.system('mpg123 ~/fabphone/voip/audio/3.mp3 &')
        time.sleep(0.5)
    if keys == [4]:
        keyboard.press('4')
        keyboard.release('4')
        os.system('mpg123 ~/fabphone/voip/audio/4.mp3 &')
        time.sleep(0.5)
    if keys == [5]:
        keyboard.press('5')
        keyboard.release('5')
        os.system('mpg123 ~/fabphone/voip/audio/5.mp3 &')
        time.sleep(0.5)
    if keys == [6]:
        keyboard.press('6')
        keyboard.release('6')
        os.system('mpg123 ~/fabphone/voip/audio/6.mp3 &')
        time.sleep(0.5)
    if keys == [7]:
        keyboard.press('7')
        keyboard.release('7')
        os.system('mpg123 ~/fabphone/voip/audio/7.mp3 &')
        time.sleep(0.5)
    if keys == [8]:
        keyboard.press('8')
        keyboard.release('8')
        os.system('mpg123 ~/fabphone/voip/audio/8.mp3 &')
        time.sleep(0.5)
    if keys == [9]:
        keyboard.press('9')
        keyboard.release('9')
        os.system('mpg123 ~/fabphone/voip/audio/9.mp3 &')
        time.sleep(0.5)
    if keys == [0]:
        keyboard.press('0')
        keyboard.release('0')
        os.system('mpg123 ~/fabphone/voip/audio/0.mp3 &')
        time.sleep(0.5)
    if keys == ['A']:
        keyboard.type('answer')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.5)
    if keys == ['B']:
        keyboard.type('@192.168.241.2')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.5)
    if keys == ['*']:
        keyboard.type('call sip:')
        os.system('mpg123 ~/fabphone/voip/audio/componi.mp3 &')
        time.sleep(0.5)
    if keys == ['C']:
        keyboard.type('bye')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.5)
    if keys == ['D']:
        keyboard.press(Key.backspace)    
        keyboard.release(Key.backspace)
        time.sleep(0.5)


