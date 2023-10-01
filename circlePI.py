import win32api, win32con, math, time, keyboard
from win32api import GetSystemMetrics

rad = math.radians
cos = math.cos
sin = math.sin

def start():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

def stop():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def move(x, y):
    win32api.SetCursorPos(
        (x, y)
    )

firstTick = False
completed = True

while True:
    if completed and keyboard.is_pressed("e"):
        completed = False

        for index in range(314 * 2):
            screenWidth = GetSystemMetrics(0)
            screenHeight = GetSystemMetrics(1)

            centerWidth = screenWidth / 2
            centerHeight = screenHeight / 2

            xyrad = index / 100

            x = cos(xyrad)
            y = sin(xyrad)
            radius = 400

            fx = centerWidth + (x * radius)
            fy = centerHeight + (y * radius)

            move(round(fx), round(fy))

            if not firstTick:
                start()
                firstTick = True

            time.sleep(0.01)

        stop()
        completed = True
