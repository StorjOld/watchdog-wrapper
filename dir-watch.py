#!/usr/bin/python
'''
Created on 2014-07-03
'''

import sys
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Extend FileSystemEventHandler to be able to write custom on_any_event method
class MyHandler(FileSystemEventHandler):
    #Overwrite the on_any_event(self,event) method with custom action
    def on_any_event(self, event):
        print (event.src_path)

# Get watch_directory parameter
watch_directory = sys.argv[1]

event_handler = MyHandler()

observer = Observer()
observer.schedule(event_handler, watch_directory, True)
observer.start()

'''
Keep the script running or else python closes without stopping the observer
thread and this causes an error.
'''
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
