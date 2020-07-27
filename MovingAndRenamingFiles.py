#From Kalle Hallden (Youtube)

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import time

class MyHandler():
    taren = "hi"
