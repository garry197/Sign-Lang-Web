def exec():    
    d = 0
    print("WELCOME TO STT(SPEECH TO TEXT) AND TTS(TEXT TO SPEECH) CONVERTER!!!")
    while(d!=5):
        print("\nTo convert speech to text in English Enter 1")
        print("To convert text to speech Enter 2")
        print("To convert text to sign language Enter 3")
        print("To convert speech to sign language Enter 4")
        print("To exit program Enter 5")
        d = int(input())
        if(d == 1):
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
                    print("Sorry could not hear you clearly. Please try again") 
        elif(d == 2):
            import pyttsx3
            engine = pyttsx3.init()
            engine.setProperty('rate',120)
            engine.setProperty('volume', 0.9)
            print("Enter the text to be converted:")
            s = input()
            engine.say(s)
            engine.runAndWait()
        elif(d == 3):
            import cv2
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            print("Enter the text to be converted:")
            h = input()
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
        
        elif(d == 4):
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
        
        elif(d == 5):
            print("Successfully exitted from program")
            exit(0)
        else:
            print("Please enter a valid input")
exec()