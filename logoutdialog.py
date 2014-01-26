#!/usr/bin/python3
# -*- coding: utf8 -*-
#
# ------------------------------------
# logoutdialog
# ------------------------------------
# logout from the system, issue a reboot
# or a  shutdown with an TickleTk GUI
# ------------------------------------

from tkinter import *
from tkinter import messagebox

import os


class LogoutDialog:
    """Dialog class for the shutdown/reboot/logout/... application"""
    def __init__(self, title):
        self.create_gui(title)
        self.loaded()

    def loaded(self):
        pass

    def are_you_sure(self, text="Bist du sicher?"):
        return messagebox.askquestion("Rückfrage", text)
        
    def create_gui(self, title):
        self.root = Tk()
        self.root.title(title)
        frame = Frame(self.root, width=400, height = 300, padx=5, pady=5)
        frame.pack()
        r=0
        c=0
        self.make_button(frame, text="Ruhemodus",
                         row=r, column=c,
                         command=self.hibernate)
        r += 1
        self.make_button(frame, text="Konsole",
                         row=r, column=c,
                         command=self.exit_openbox)
        r += 1
        self.make_button(frame, text="Neustart",
                         row=r,column=c,
                         command=self.reboot)
        r += 1
        self.make_button(frame, text="Ausschalten",
                         row=r,column=c,
                         command=self.shutdown)
        r += 1
        self.make_button(frame, text="Abbrechen",
                         row=r,column=c,
                         command=self.cancel)
        r += 1

    def mainloop(self):
        """enters the main loop of Tk"""
        self.root.mainloop()

    def close(self):
        """close this application"""
        self.root.destroy()

    def make_button(self, parent, text="Button", command=None, row=0, column=0):
        """create a new button widget"""
        but = Button(parent, text=text, command=command, relief='flat', padx=5, pady=5)
        but.grid(row=row, column=column, sticky=EW)
        return but
        
    def cancel(self):
        """callback for cancel-button"""
        self.close()

    def reboot(self):
        """callback for reboot-button"""
        if self.are_you_sure("Bist du sicher, dass du den Rechner neu starten willst?")=='yes':
            ret = os.system("sudo shutdown -r now")

    def exit_openbox(self):
        """callback for openbox exit, back to conole"""
        if self.are_you_sure("Bist du sicher, dass du zur Konsole zurück willst?")=='yes':
            ret = os.system("openbox --exit")

    def shutdown(self):
        """callback for shutdown-button"""
        if self.are_you_sure("Bist du sicher, dass du den Rechner herunterfahren willst?")=='yes':
            ret = os.system("sudo shutdown -h now")
        
    def hibernate(self):
        """callback for hybernate button"""
        if self.are_you_sure()=='yes':
            ret = os.system("gdm-control --suspend")

if __name__ =="__main__":
    cls = LogoutDialog("Logoff")
    cls.mainloop()
