#From Kalle Hallden (Youtube)

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            count=0
            for i in reversed(range(len(filename))):
                if filename[i]=="." and count==0:
                    indexval=i
                    count=1
            filetype=filename[indexval:]
            time.sleep(2)
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src,new_destination)
            print(filetype)

folder_to_track = "C:/Users/taren/Desktop/TestingFolder/Folder1"
folder_destination = "C:/Users/taren/Desktop/TestingFolder/Folder2"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()