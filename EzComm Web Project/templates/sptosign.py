# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:47:43 2019

@author: Sukruth
"""

def exec4():
    import speech_recognition as sr 
    mic_name = "Microphone (Realtek Audio)"
    sample_rate = 48000
    chunk_size = 2048
    r = sr.Recognizer() 
    mic_list = sr.Microphone.list_microphone_names() 
    for i, microphone_name in enumerate(mic_list): 
        if microphone_name == mic_name: 
            device_id = i 
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  chunk_size = chunk_size) as source: 
            r.adjust_for_ambient_noise(source) 
            print("Say Something")
            audio = r.listen(source) 
            try: 
                text = r.recognize_google(audio) 
                print("You said: " + text)
            except sr.UnknownValueError:
                text = "Sorry could not hear you clearly. Please try again"
                print("Sorry could not hear you clearly. Please try again")
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
        startfile("C:/Users/Sukruth/Desktop/EzComm Web Project/templates/video.mp4")