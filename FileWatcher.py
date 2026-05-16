from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd
import time
import os

os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".input.csv"):

            print("New file:", event.src_path)

            time.sleep(2)  # wait for file to finish copying

            df = pd.read_csv(event.src_path)

            df["processed"] = True

            filename = os.path.basename(event.src_path)
            df.to_csv(f"output/{filename}", index=False)

            print("Processed:", filename)

observer = Observer()
observer.schedule(Handler(), path="input", recursive=False)

observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()

observer.join()