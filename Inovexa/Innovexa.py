
import speech_recognition as speech
import pyttsx3
import pygame
import keywords as keys

engine=pyttsx3.init()
engine.setProperty('rate',150)

pygame.init()

width=900
height= 600
screen=pygame.display.set_mode( ( width, height) )

pygame.display.set_caption('Innovexa')

bg=pygame.image.load("Images/g1.png")
image1=pygame.transform.scale(bg, (900,600))
screen.blit(image1,(0,0))
pygame.display.update()

activate="none"
exitstatus="no"

while True:
    try:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    activate = 'c'
                    print("C pressed")
                    
        if activate=='c':
            listenImg=pygame.image.load("Images/g2.png").convert_alpha()
            image1=pygame.transform.scale(listenImg, (900,600))
            screen.blit(image1,(0,0))
            pygame.display.update()
            
            r=speech.Recognizer()
            
            with speech.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Speak:")
                    audio=r.listen(source)
         
            command=r.recognize_google(audio).lower()
                
            print("You said: "+command)
            
            for keyword in keys.inventions:
                
                if keyword in command:
                        
                        if keys.inventions[keyword][0]=="imgSpch":
                            print(keys.inventions[keyword][2])
                            
                            image=pygame.image.load("Images/"+keys.inventions[keyword][2]+".jpg").convert_alpha()
                            image1=pygame.transform.scale(image, (813,375))
                            screen.blit(image1,(45,145))
                          
                            pygame.display.update()
                            
                            engine.say(keys.inventions[keyword][1])
                            engine.runAndWait()
                         
                        if keys.inventions[keyword][0]=="exit":
                            engine.say(keys.inventions[keyword][1])
                        engine.runAndWait()
                        exitstatus="yes"
                        break    
                    
            if exitstatus=="yes":
                    pygame.quit()
                    break

            activate="none" 
            bg=pygame.image.load("Images/g1.png").convert_alpha()
            image1=pygame.transform.scale(bg, (900,600))
            screen.blit(image1,(0,0))
        
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
    

           
                



