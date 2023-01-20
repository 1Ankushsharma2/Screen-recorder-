import cv2                             #cv2 is func to all sc to merge to make a video 
import pyautogui                       #pyautogui use to screen recodring related
from win32api import GetSystemMetrics     # win32 use to screen resulations
import numpy as np                      #numpy ue to arry all screen shot to save them
import time
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
dim=(width,height)
f=cv2.VideoWriter_fourcc(*"XVID")  #xvid giong to save our video .mp4 or anythik ese format
output=cv2.VideoWriter("test.mp4",f,30.0,dim)    #freame per sec(f,30.0)
now_start_time=time.time()
dur=10+4
end_time=now_start_time + dur
while True:
    image=pyautogui.screenshot()      #pyautogui take screenshot for video
    frame_1=np.array(image)           #all screenshot goes to fram to make a video
    frame=cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)   #this will take  og colour save colorrgr2...
    output.write(frame)
    c_time=time.time()
    if c_time>end_time:
        break
output.release()
print("Recording End")    