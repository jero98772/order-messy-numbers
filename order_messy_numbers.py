import numpy as np
import time
import subprocess
subprocess.run("touch lista.txt",shell=True)
start=time.time()
size=1000
num=-1
tmp=1
count=0
itr=0
vec=np.array([])
rng=np.random.default_rng()
vector=rng.choice(size,size=size,replace=False)
#vector=np.random.randint(size ,size=size)
print(vector)

input("lets go")
for x in vector:

       select=x
       while itr< size:

         if  itr != vector[itr]:

         # time.sleep(1)
          if vector[itr]>itr:
                
                itr+=1
                print(">")

                print("cuenta",itr,"\ncuent2",count)
                vec=np.append(vec,itr)
                print(vec)
                break
          elif vector[itr] < itr:
             
                itr+=1
                print("<")
                print("cuenta",itr,"\ncuent2",count)
                vec=np.append(vec,itr)
                print(vec)
                num+=1
                tmp+=1
                break
         elif  vector[itr]== itr:
             if num<select<tmp:
                print("==")
                print("cuenta",itr,"\ncuent2",count)
                itr+=1
                num+=1
                tmp+=1
                vec=np.append(vec,itr)
                print(vec)
                break
print(vec)
print("\n\n")
print(vector,"\n","\t"*5)
print("        ") 
print("   /\   ")
print("  /  \   ") 
print(" / _  \  ")
print("/_/ \__\ ")
print("  | |    ")
print("  | |    ")
print("  | |    ")
print("  |_|    ")
print("      ")
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
