import subprocess
import webbrowser
import keyboard

def open_whatsapp():
    # Open WhatsApp Web URL in the default web browser
    webbrowser.open('https://web.whatsapp.com/')

def on_key_event(e):
    if keyboard.is_pressed('win+w'):
        open_whatsapp()

keyboard.hook(on_key_event)
keyboard.wait('esc')  # Wait for the user to press 'esc' to exit the program
