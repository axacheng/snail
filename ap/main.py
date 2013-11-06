#!/usr/bin/env python
import wx
import time
import os
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ChangeHandler(FileSystemEventHandler):

    def set_message_obj(self, message):
        self.message = message

    def on_any_event(self, event):
        pass
        # self.message.SetValue(self.message.GetValue() + "\n" + event.src_path)

    def on_created(self, event):
        self.message.SetValue(self.message.GetValue() + "\nCreate file : " + event.src_path)

    def on_deleted(self, event):
        self.message.SetValue(self.message.GetValue() + "\nDelete file : " + event.src_path)

    def on_modified(self, event):
        self.message.SetValue(self.message.GetValue() + "\nModified file : " + event.src_path)

    def on_moved(self, event):
        self.message.SetValue(self.message.GetValue() + "\nMove file : " + event.src_path)        

class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600,400))
        self.message = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.message.SetValue("monitor folder is " + os.getcwd())
        self.CreateStatusBar()
        self.Show(True)

class GuiThread(threading.Thread):
    def __init__(self, event_handler):
        threading.Thread.__init__(self)
        self.app = wx.App(False)
        self.frame = MainWindow(None, "snail client ver 0.0.1")
        self.frame.Centre()
        event_handler.set_message_obj(self.frame.message)
        self.app.MainLoop()

if __name__ == "__main__":

    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, os.getcwd(), recursive=False)
    observer.start()

    wxThread = GuiThread(event_handler)
    wxThread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
