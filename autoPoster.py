#!/usr/bin/env python

# -*- coding: utf-8 -*-

import pyperclip
import pyautogui
import time
import string

string="your text" #string text
f = open('groups.txt','r') #Group id must be in text file example:121545789562
groups=[]
for line in f:
    groups.append(line.strip())
time.sleep(5)

pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')

for i in range(len(groups)):
    link = 'https://facebook.com/groups/'+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')

    print("Waiting for 12 seconds\n")
    time.sleep(12)

    pyautogui.typewrite('p')
    time.sleep(2)
    print("Writing post\n")

    for char in string:#for Unique  Characters
        pyperclip.copy(char)
        pyautogui.hotkey('ctrl','v')

    print("done")
    time.sleep(2)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')

    time.sleep(3)

    pyautogui.write(['f6'])
    time.sleep(1)