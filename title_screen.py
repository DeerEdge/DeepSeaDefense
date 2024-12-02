from cmu_graphics import *
from check_functions import *
from game_screen import *
from mapeditor_screen import *

def onAppStart(app):
    app.color = "blue"
    app.width, app.height = 1000, 700
    app.pointerColor = "red"
    app.pointerLocation = (0, 0)

def title_redrawAll(app):
    # Draw background
    drawRect(0, 0, 1000, 700, fill=gradient('darkTurquoise', 'dodgerBlue', 'darkBlue', start='top'), opacity=100)

    # Draw leftside characters
    drawStar(150, 20, 350, 20, fill='fireBrick', opacity=100, align='center', roundness=95)
    drawStar(150, 20, 350, 20, fill='black', opacity=80, align='center', roundness=95)
    drawStar(0, 650, 350, 20, fill='fireBrick', opacity=100, align='center', roundness=95)
    drawStar(0, 650, 350, 20, fill='black', opacity=80, align='center', roundness=95)
    drawImage("assets/images/title_screen/queen.png", -70, 190, width=350, height=350)
    drawImage("assets/images/title_screen/serpent.png", 120, 320, width=280, height=280)
    drawImage("assets/images/title_screen/slither.png", 170, 500, width=250, height=250)
    drawImage("assets/images/title_screen/leeching-worm.png", -40, 435, width=300, height=300)

    # Draw rightside characters
    drawCircle(970, -560, 800, fill='black', opacity=100, align='center')
    drawCircle(1200, 650, 550, fill='black', opacity=100, align='center')
    drawCircle(1200, -50, 550, fill='black', opacity=100, align='center')
    drawImage("assets/images/towers/monster-net.png", 450, -100, width=150, height=150)
    drawImage("assets/images/towers/magic-portal.png", 600, -20, width=150, height=150)
    drawImage("assets/images/towers/resource-mine.png", 780, -30, width=150, height=150)
    drawImage("assets/images/towers/missile-mech.png", 830, 130, width=150, height=150)
    drawImage("assets/images/towers/laser-turret.png", 690, 450, width=150, height=150)
    drawImage("assets/images/towers/tesla-coil.png", 810, 290, width=170, height=170)
    drawImage("assets/images/towers/pulsar-tower.png", 850, 520, width=150, height=150)
    drawImage("assets/images/towers/tooth-trap.png", 680, 600, width=150, height=150)

    # Draw title and buttons
    drawRect(app.width // 2, app.height // 5, app.width // 1.3, app.height // 5, align='center',
             fill=gradient('dodgerBlue', 'darkBlue', 'navy', start='top'), border='white', borderWidth=1, opacity=80)
    drawLabel('Deep Sea Defense', app.width // 2, app.height // 5, fill='white', size=80, bold=True, italic=True,)
    drawRect(app.width // 2, app.height // 2 - 50, app.width // 4, app.height // 10, align='center', fill='black',
             border='white', borderWidth=1, opacity=80)
    drawRect(app.width // 2, app.height // 2 + 40, app.width // 4, app.height // 10, align='center', fill='black',
             border='white', borderWidth=1, opacity=80)
    drawRect(app.width // 2, app.height // 2 + 130, app.width // 4, app.height // 10, align='center', fill='black',
             border='white', borderWidth=1, opacity=80)
    drawLabel('Start Game!', app.width // 2, app.height // 2 - 50, fill='white', size=30, bold=True)
    drawLabel('Rulebook', app.width // 2, app.height // 2 + 40, fill='white', size=30, bold=True)
    drawLabel('Map Editor', app.width // 2, app.height // 2 + 130, fill='white', size=30, bold=True)

    drawCircle(app.pointerLocation[0], app.pointerLocation[1], 5, fill=app.pointerColor)

def title_onMousePress(app, mouseX, mouseY):
    app.pointerColor = 'lightgreen'
    if isWithinRect(app.width // 2, app.height // 2 - 50, app.width // 4, app.height // 10, mouseX, mouseY):
        setActiveScreen('game')
    elif isWithinRect(app.width // 2, app.height // 2 + 130, app.width // 4, app.height // 10, mouseX, mouseY):
        setActiveScreen('mapeditor')

def title_onMouseMove(app, mouseX, mouseY):
    app.pointerColor = 'red'
    app.pointerLocation = (mouseX, mouseY)

def main():
    runAppWithScreens(initialScreen='title')

main()
