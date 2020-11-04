# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:44:04 2020

@author: HP
"""

import pyautogui
import time
import keyboard
import win32api,win32con

time.sleep(3)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q')==False:
    pic=pyautogui.screenshot(region=(584,425,750,522))
    width,height=pic.size
    
    for x in range(0,width,5):
        for y in range(0,height,5):
            r,g,b=pic.getpixel((x,y))
            if b==195:
                click(x+584,y+425)
                time.sleep(0.09)
                break
                
            

