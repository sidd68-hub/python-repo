import rumps
import subprocess
import signal
import os

class StayAwakeApp(rumps.App):
    def __init__(self):
        super(StayAwakeApp, self).__init__("☕ StayAwake", quit_button="Quit")
        self.caffeinate_proc = None
        self.menu = ["Start", "Stop"]
        self.icon = None  # optional: set your own .icns

    @rumps.clicked("Start")
    def start_awake(self, _):
        if self.caffeinate_proc is None:
            self.caffeinate_proc = subprocess.Popen(["caffeinate", "-d", "-i", "-s", "-u"])
            rumps.notification("Stay Awake", "Running", "Your Mac will stay awake")
        else:
            rumps.notification("Stay Awake", "Already running", "Your Mac is already kept awake")

    @rumps.clicked("Stop")
    def stop_awake(self, _):
        if self.caffeinate_proc is not None:
            os.kill(self.caffeinate_proc.pid, signal.SIGTERM)
            self.caffeinate_proc = None
            rumps.notification("Stay Awake", "Stopped", "Your Mac can now sleep")
        else:
            rumps.notification("Stay Awake", "Not running", "No awake process running")

if __name__ == "__main__":
    StayAwakeApp().run()
