# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 02:15:21 2020

@author: HP
"""

import pyautogui
from time import sleep
sleep(10)
f=open("beemovie.txt",'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
      
   