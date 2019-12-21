# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:46:42 2019

@author: Sukruth
"""

        
def exec3(text):
    import cv2
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    h = text
    no_punct = ""
    for char in h:
        if char not in punctuations:
            no_punct = no_punct + char
    l = []
    l.extend(no_punct)
            
    video_name = 'video.mp4'
    images = []
    for x in l:
        if(x!=" "):
            images.append("{}.jpg".format(x.upper()))
        else:
            images.append("dot.jpg")
    images.append("dot.jpg")
    images.append("dot.jpg")
                
    frame = cv2.imread(images[0])
    height, width, layers = frame.shape
            
    video = cv2.VideoWriter(video_name, 0, 1, (width,height))
    for image in images:
        video.write(cv2.imread(image))
                
    cv2.destroyAllWindows()
    video.release()
    from os import startfile
    startfile("video.mp4") 
            
                     