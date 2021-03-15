import pyautogui
import time

rows = int('1') #insert number of rows you would like to type
columns = int('25') #insert number of columns you would like to type

for i in range(columns):
    time.sleep(1) #insert a gap(in secunds) between sending messages
    pyautogui.typewrite("word" * rows) #insert any word or phrase you would like to type
    pyautogui.press("enter")
