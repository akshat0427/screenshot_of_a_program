
from tkinter import filedialog as fd
import time
import os
import pygetwindow
import pyautogui
from PIL import Image


def open_file_selection():
    file = fd.askopenfile()
    return file.name

path_ = open_file_selection()

os.system(f"code . {path_}")
titles = pygetwindow.getAllTitles()



for i in titles:
    # print(i)
    if 'Code' in i:
        
        vs_code_window = i
        
def screenshot(window):
    
    path = '''.\_automated_screenshot.jpg'''
   
    window = pygetwindow.getWindowsWithTitle(window)[0]
    
    left, top = window.topleft
    right,bottom = window.bottomright
    pyautogui.screenshot(path)

    im = Image.open(path)
    im = im.crop((left, top, right, bottom))
    im.save(path)
    
time.sleep(3)

screenshot(vs_code_window)

