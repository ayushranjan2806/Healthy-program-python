import datetime
import time
import pygame
from pygame import mixer
def gettime():
    return datetime.datetime.now()


def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper :
            mixer.music.stop()
            break

def log_now(msg):
   with open ("rountine.txt","a") as f:
        f.write(str([str(gettime())]) + ":" + msg + "\n")
        print(" data is successfully updated")
        # speak(" data is sucessfully  save in your covid file")
        

if __name__ == '__main__':
    watersecs=2
    exsecs=4
    eyessecs=6
    water_time=time.time()
    eye_time=time.time()
    excer_time=time.time()

    while True:
        if time.time()-water_time > watersecs :
            print("water drinking time .enter 'DRANK'to stop the alarm")
            musiconloop('songs.mp3','drank')
            water_time=time.time()
            log_now("drank water at ")
        if time.time()-excer_time > exsecs :
            print("type 'stop' to stop the alarm")
            musiconloop('songs.mp3','rukaja')
            excer_time=time.time()
            log_now("excerise done at ")
        if time.time()-eye_time > eyessecs:
            print("type 'DONE' to stop the alarm")
            musiconloop('eyes.mp3.mp3','drank')
            eye_time=time.time()
            log_now("eyesmonitoring done at ")    
                



   
    