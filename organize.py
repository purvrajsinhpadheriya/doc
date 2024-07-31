import os
import shutil 
import sys
import time
import random
 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
 
from_dir = "C:/Users/BRIGHT/OneDrive/Desktop"
to_dir = "C:/Users/BRIGHT/Downloads"

dictionary = (
"Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
"Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif']
"Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
"Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
)

class filemovement(filesystem):
    def createon(self,event)
    
    list_of_file = os.listdir(from_dir)
    name,extention = os.path.splitext(event.src_path)
    for key,value in dictionary.items():
                     
    if extention  =="":
        continue
    if extention in value:
        file_name = os.path.basename(event.src_path)
        path1  = from_dir +"/"+file_name
        path2 = to_dir + "/"+key
        path3 = to_dir + "/" + key + "/" + file_name
        if os.path.exists(path2):
            print("moving"+file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+file_name)
            shutil.move(path1,path3)
               
eventhandler = filemovement()
observer = Observer()
observer.schedule(eventhandler,from_dir,recursive = True)
observer.start()
try : 
    while True : 
        time.sleep(2)
        print("runing..")
except KeyboardInterrupt:
    print("stop")
    observer.stop        
