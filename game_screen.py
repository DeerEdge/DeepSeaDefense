from cmu_graphics import *
from check_functions import *

def game_redrawAll(app):
    drawLabel('Started', app.width // 2, app.height // 5, size=80, font="monospace", bold=True)
    drawRect(10, 10, 790, 590, fill='white', border='black', borderWidth=2)
    drawLabel('Towers', 900, 30, size=30, font="monospace", bold=True)
    for posX in range(2):
        for posY in range(6):
            drawRect(810 + posX*90, 50 + posY*90, 85, 85, fill='white', border='black', borderWidth=2)
