# coding: utf-8
import json
import pathlib
from collections import Counter

from apscheduler.schedulers.background import BackgroundScheduler
from pynput import keyboard


# file writing
class Recorder:
    def __init__(self):
        self.recorder_d = Counter()
        self.user_path = pathlib.Path.home() / "KeyboardInputRecord.json"
        self.fd_func = lambda: open(self.user_path, "w", encoding="utf-8")

    def record(self, s: str) -> None:
        self.recorder_d.update([s])

    def save(self):
        self.fd_func().write(json.dumps(self.recorder_d, indent=4))


recorder = Recorder()

schedule = BackgroundScheduler()
schedule.add_job(recorder.save, "interval", seconds=10)
schedule.start()


class ListenerFunc:
    @staticmethod
    def release(key):
        # pass
        recorder.record(str(key))

    @staticmethod
    def press(key):
        # recorder.record(str(key))
        pass


print(f"Start Record Key Input to {recorder.user_path}")

# listener
with keyboard.Listener(on_press=ListenerFunc.press, on_release=ListenerFunc.release) as key_listener:
    key_listener.join()
