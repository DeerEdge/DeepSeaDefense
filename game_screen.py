from cmu_graphics import *
from check_functions import *

def game_redrawAll(app):
    drawLabel('Started', app.width // 2, app.height // 5, size=80, font="monospace", bold=True)
    drawRect(10, 10, 790, 590, fill='white', border='black', borderWidth=2)
