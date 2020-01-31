import numpy as np
from pygame.mixer import Sound
import pygame
import time
import subprocess
subprocess.run("touch lista.txt",shell=True)
size=eval(input("enter a int number"))
num=-1
tmp=1
count=0
itr=0
delay=2
vec=np.array([])
rng=np.random.default_rng()
vector=rng.choice(size,size=size,replace=False)
#vector=np.random.randint(size ,size=size)
print(vector)
pygame.init()
tv=Sound("soundTv.wav")
buzz=Sound("buzz.wav")
radar=Sound("radar.wav")
input("lets go")
pygame.mixer.music.set_volume(0.5)

start=time.time()
for x in vector:
    
       buzz.fadeout(10)
       tv.fadeout(10)
       radar.fadeout(20)
       delay = delay /200
       time.sleep(delay)
       #print(delay)
       buzz.stop()
       tv.stop()
       radar.stop()
       if (itr+1 % tmp)!=0:
         #buzz.play(size,0.5)
            #print("zhhh")
            buzz.play()
            if itr>25:
              radar.play()  
              tv.play()
            #buzz.stop()
            
            tv.stop()
       elif (itr+1 % tmp)==0:
           buzz.stop()
           tv.play()
           #time.sleep(0.5)
           #tv.stop()
       select=x
       while itr< size:
         time.sleep(0.5)
         if  itr != vector[itr]:

          #time.sleep(0.0001)
          if vector[itr]>itr:
                
                itr+=1
                print(">")

                print("cuenta",itr)#,"\ncuent2",count)
                vec=np.append(vec,itr)
                #print(vec)
                break
          elif vector[itr] < itr:
             
                itr+=1
                print("<")
                print("cuenta",itr)#,"\ncuent2",count)
                vec=np.append(vec,itr)
                #print(vec)
                num+=1
                tmp+=1
                break
         elif  vector[itr]== itr:
             if num<select<tmp:
                print("==")
                print("cuenta",itr)#,"\ncuent2",count)
                itr+=1
                num+=1
                tmp+=1
                vec=np.append(vec,itr)
                break               
                #print(vec)


print(vec)
print("\n\n")
print(vector,"\n","\t"*5)
print("                   ") 
print("             ^     ") 
print("            / \    ")
print("           /   \   ") 
print("          /     \  ")
print("         /__/ \__\ ")
print("            | |    ")
print("            | |    ")
print("            | |    ")
print("            |_|    ")
print("                    ")
print(" _       _   _                                               ")
print("(_)___  | |_| |__   ___    __ _ _ __  _____      _____ _ __  ")
print("| / __| | __| '_ \ / _ \  / _` | '_ \/ __\ \ /\ / / _ \ '__| ")
print("| \__ \ | |_| | | |  __/ | (_| | | | \__ \\\ V  V /  __/ |    ")
print("|_|___/  \__|_| |_|\___|  \__,_|_| |_|___/ \_/\_/ \___|_|    ")


archivo1=open("lista.txt",'w')
stop=time.time()
text=str(vec)+"\n \n \n"+str(vector)+"\n"+"\t"*5+"your time is   "+str(stop-start)
archivo1.write(text)
print("your time is",stop-start)
