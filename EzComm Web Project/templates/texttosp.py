# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:45:46 2019

@author: Sukruth
"""

def exec2(text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate',120)
    engine.setProperty('volume', 0.9)
    s = text
    engine.say(s)
    engine.runAndWait()