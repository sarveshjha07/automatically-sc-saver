# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:51:44 2020

@author: sarve
"""
from selenium import webdriver
import time
links = ['dev.to', 'twitter.com', 'github.com']
with webdriver.Chrome("D:/chrome_driver_for practice/chromedriver") as driver:#yaha mera chrome driver ka path hai change according to your convinence.  
    for link in links:
        desktop = {'output': str(link) + '-desktop.png','width': 2200,'height': 1800}
        linkWithProtocol = 'https://' + str(link)
        # set the window size for desktop
        driver.set_window_size(desktop['width'], desktop['height'])
        driver.get(linkWithProtocol)
        time.sleep(1)
        driver.save_screenshot(desktop['output'])
    driver.quit()
print("end...")