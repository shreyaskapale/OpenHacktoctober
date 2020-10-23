from ctypes import Structure, windll, c_uint, sizeof, byref
import keyboard
import time
class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

while True:
    t=get_idle_duration()
    if(t>20):
        keyboard.press_and_release('page down')
        time.sleep(30)
    else:
        continue
